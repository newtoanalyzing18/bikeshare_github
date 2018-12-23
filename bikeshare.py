import time
import pandas as pd
import numpy as np

cities = ['chicago','new york city','washington']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - number of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('What city would you like to view: ').lower()
            if city in cities:
                break
            else:
                print('That is not a valid city. Try New York City, Chicago, or Washington')
        except:
            print('There was an unknown error')
        finally:
            print('\nAttempted Input\n')

    # get user input for month (all, january, february, ... , june) make sure these are integers
    while True:
        try:
            month = input("Filter on what month (select all for all months) "
                          "give as an integer: ")
            if month in str(range(1,7)):
                break
            elif month.lower() == 'all':
                break
            else:
                print('That is not a valid month. Try an integer 1-7')
        except:
            print('There was an unknown error')
        finally:
            print('\nAttempted Input\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Filter on what day of the week(select all for all days): ")
            if day in str(range(1,8)):
                break
            elif day.lower() == 'all':
                break
            else:
                print('That is not a valid day. Try an integer 1-7')
        except:
            print('There was an unknown error')
        finally:
            print('\nAttempted Input\n')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    # read and load city data frame
    df = pd.read_csv('./{}.csv'.format(city))
    # convert times from string to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # filter by selected month
    if month == 'all':
        df
    else:
        df = df[(df['Start Time'].dt.month == int(month))]

    # filter by selected day
    if day == 'all':
        df
    else:
        df = df[(df['Start Time'].dt.dayofweek == int(day))]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most popular month(s):')

    print(df['Start Time'].dt.month.value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['Start Time'].dt.month.value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['Start Time'].dt.month.value_counts().iloc[left:right])
        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    # display the most common day of week
    print('Most popular day of the week(s):')
    print(df['Start Time'].dt.dayofweek.value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['Start Time'].dt.dayofweek.value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['Start Time'].dt.dayofweek.value_counts().iloc[left:right])

        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    # display the most common start hour
    print('Most popular start hour(s):')
    print(df['Start Time'].dt.hour.value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['Start Time'].dt.hour.value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['Start Time'].dt.hour.value_counts().iloc[left:right])

        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most popular start station(s):')
    print(df['Start Station'].value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['Start Station'].value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['Start Station'].value_counts().iloc[left:right])

        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    # display most commonly used end station
    print('Most popular end station(s):')
    print(df['End Station'].value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['End Station'].value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['End Station'].value_counts().iloc[left:right])

        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    # display most frequent combination of start station and end station trip
    df['End & Start Station'] = df['Start Station'] + df['End Station']
    print('Most frequent station combo(s):')
    print(df['End & Start Station'].value_counts().iloc[0:5])
    left = 0
    right = 5
    while True:
        if df['End & Start Station'].value_counts().iloc[left:right].empty:
            print('No more results. Move along :)')
            break
        more_data = input('\nWould you like to see more? Enter yes or no.\n').lower()
        if more_data =='yes':
            left += 5
            right += 5
            print(df['End & Start Station'].value_counts().iloc[left:right])

        elif more_data.lower() not in ['yes','no']:
            print('Try again. Enter yes or no')
            continue
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total))

    # display mean travel time
    avg = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds'.format(avg))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type counts:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('User gender counts:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('This file has no gender data')

    # Display earliest, most recent, and most common year of birth
    print('User birth year:')
    try:
        earliest = min(df['Birth Year'])
        most_recent = max(df['Birth Year'])
        most_common = df['Birth Year'].value_counts().index.tolist()[0]
        print('Birth Years:\nEarliest: {}\nMost Recent: {}\nMost Common: {}'
              .format(earliest, most_recent, most_common))
    except:
        print('This file has no birth year data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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