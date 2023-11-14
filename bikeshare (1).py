import time
import pandas as pd
import numpy as np

# code begins
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input('Enter city (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please enter a valid city.')

    # Get user input for month
    month = input('Enter month (all, January, February, ..., June): ').lower()

    # Get user input for day of week
    day = input('Enter day of week (all, Monday, Tuesday, ..., Sunday): ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # Loads data for the specified city and filters by month and day if applicable.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of the week'] = df['Start Time'].dt.day_name()

    # Args:
    """
    (str)city : name of the city to analyze
    (str)month : name of the month to filter by, or "all" to apply no month filter
    (str)day : name of the day of week to filter by, or "all" to apply no day filter
    """
    # Returns:
    """
            df - Pandas DataFrame containing city data filtered by month and day
    """
    if month != 'all':
        df = df[df['Month'] == MONTHS.index(month) + 1]
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode().iloc[0]
    print(most_common_month)

    # TO DO: display the most common day of week
    most_common_week_day = df['Day of week'].mode().iloc[0]
    print(most_common_week_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['Hour'].mode().iloc[0]
    print(most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode().iloc[0]

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode().iloc[0]

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print(count_of_user_types)

    # Check if 'Gender' and 'Birth Year' columns are present
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode().iloc[0]
    else:
        print('\nGender and Birth Year information not available for this dataset.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """
    Displays 5 rows of individual trip data upon user request.

    Args:
    df: Pandas DataFrame containing city data.

    Returns:
    None
    """
    start_loc = 0

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()

    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
