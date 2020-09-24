import time
import pandas as pd
import numpy as np
# We create some variables. change made for version control project
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''
    while city.lower() not in city_names:
        city = input("Which city would you like to explore? Chicago, New_York_City or Washington?\n")
        if city.lower() in city_names:
            city=city.lower()
            #if the selection is correct
            print("\nThanks, let's continue\n")
        else:
            #If we don't get a valid selection
            print("\nWe are sorry, you have selected a not valid city. Please, try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june).CHANGE MADE FOR VC PROJECT 1

    month = ''
    while month.lower() not in month_names:
        month = input("\nWich month would you like to explore? all, january, february,...,june?\n")
        if month.lower() in month_names:
            month = month.lower()
            #if we get the right month name
            print("\nThanks, let's continue\n")
        else:
            #If we don't get a valid answer
            print("\nWe are sorry, you have selected a not valid month. Please, try again.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    while day.lower() not in day_names:
        day = input("\nwich day of week would you like to explore? all, monday, tuesday,...sunday?\n")
        if day.lower() in day_names:
            day = day.lower()
            print("\nThanks, let's continue\n")

            #if we get the right day name
        else:
            #If we don't get a valid answer
            print("\nWe are sorry, you have selected a not valid input. Please, try again.\n")
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data
    df = pd.read_csv(CITY_DATA[city])
    # Convert to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june'] #get the index
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most common month is: \n", popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("\nThe most common day of week is: \n", popular_day_of_week)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print("\nThe most common start hour is: \n" , str(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station is:\n', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is:\n', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    popular_combination = df['combination'].mode()[0]
    print('\nThe most common combination is: \n', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\n The total travel time is:\n', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\n The mean travel time is:\n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n The user types counting for the selection is:\n', user_types)
    # TO DO: Display counts of gender
    if city != 'washington':

        counts_gender = df['Gender'].value_counts()
        print('\n The number of males and females is:\n', counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        oldest_person_yearofbirth = df['Birth Year'].min()
        print('\nThe oldest person born on:\n', oldest_person_yearofbirth)
        youngest_person_yearofbirth = df['Birth Year'].max()
        print('\nThe youngest person born on:\n', youngest_person_yearofbirth)
        popular_yearofbirth = df['Birth Year'].mode()[0]
        print('\nThe most popular year of birth is:\n', popular_yearofbirth)
    else:
        print("\nThe selected city doesn't have this information")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x =  1
    while True:
        rows = input('\nWould you like to see some raw data? write yes or no.\n')
        if rows.lower() == 'yes':
            x = x+5
            print(df[x:x+5])
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
