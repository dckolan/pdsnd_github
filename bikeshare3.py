import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    city = input('Would you like to see date for Chicago, New York City, or Washington? ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Error. Would you like to see date for 'Chicago', 'New York City', or 'Washington'? ").lower()

    time_filter = input('Would you like to filter the data by month, day, both or neither? ').lower()
    while time_filter not in ['month', 'day', 'both', 'neither']:
        time_filter = input ("Error. Would you like to filter the data by 'month', 'day', 'both' or 'neither'? ").lower()

    if time_filter == 'month':
        day = 'none'

    if time_filter == 'day':
        month = 'none'

    if time_filter == 'neither':
        month = 'none'
        day = 'none'

    if time_filter == 'both' or time_filter == 'month':
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Which month? January, February, March, April, May, or June? ').lower()
        while month not in ['january', 'february', 'march', 'april', 'may','june']:
            month = input ("Error. Which month? 'January', 'February', 'March', 'April', 'May', or 'June'? ").lower()

    if time_filter == 'both' or time_filter == 'day':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday? ').lower()
        while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            day = input ("Error. Which day? 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', or 'Saturday'? ").lower()

    print('-'*40)

    return city, time_filter, month, day

def load_data(city, time_filter, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if time_filter == 'both' or time_filter == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    if time_filter == 'both' or time_filter == 'day':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    trip = (df['Start Station']+" to "+df['End Station']).mode()[0]
    print('Most Common Trip:', trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time Is:', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time Is:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of Each User Type Is:', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Count of Each Gender Is:', gender)
    except:
        print('User Info Unavailable')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest Birth Year Is:', earliest_birth_year)
        print('Most Recent Birth Year Is:', most_recent_birth_year)
        print('Most Common Birth Year Is:', most_common_birth_year)
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    raw = input('Do you want to see five lines of raw data? ').lower()
    while raw not in ['yes','no']:
        raw = input ("Do you want to see five lines of raw data? Enter 'yes' or 'no'. ").lower()
    x = 0
    while raw == 'yes':
        x = x+5
        print(df.head(x))
        raw = input('Do you want to see more five lines of raw data? ').lower()
        while raw not in ['yes','no']:
            raw = input ("Do you want to see five lines of raw data? Enter 'yes' or 'no'. ").lower()

def main():
    while True:
        city, time_filter, month, day = get_filters()
        df = load_data(city, time_filter, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes','no']:
            restart = input ("Would you like to restart? Enter 'yes' or 'no'. ").lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
    
