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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Please enter Chicago, Washington or New York City for your analysis:").lower()
       
        if city in ['chicago', 'new york city', 'washington'] :
          
            break
    else:
        print("invalid input")


         


         

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter any one of the first 6 months or enter All to select all 6 months:").lower()
       
        if month in ['all','january','february','march','april','may','june'] :
          
            break
    else:
        print("invalid input")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("please choose name of the day of week to filter by, or all to apply no day filter : ").lower()
       
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
          
            break
    else:
        print("invalid input")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    if month!='all':
        
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df = df[df['month'] == month]
 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month is: ',df['month'].mode()[0])

    # display the most common day of week
    print('the most common day of week: ',df['day_of_week'].mode()[0])   

    # display the most common start hour
    print("the most common start hour:",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station is: ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station is: ',df['End Station'].mode()[0]) 

    # display most frequent combination of start station and end station trip
    frequent_comb = df['Start Station'] + df['End Station'].mode()[0]
    print('most frequent combination of start station and end station trip: ',frequent_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time:', round(df['Trip Duration'].sum()),"Seconds")

    # display mean travel time
    print('mean travel time: ',round(df['Trip Duration'].mean()),"Seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    
    print('counts of user types: ',df['User Type'].value_counts())   

    # Display counts of gender
    try:
        print('counts of gender:',df['Gender'].value_counts())
    except:
            print("there is no cloums for Gender")

    # Display earliest, most recent, and most common year of birth
    try:
       print('earliest year:',int(df['Birth Year'].min()))
       print('Most Recent Year:',int(df['Birth Year'].max()))
       print('Most Common Year:',int(df['Birth Year'].mode()))
    except:
         print("there is no cloums for Birth Year")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("would like to see the raw data?  ").lower()# TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("would you like to see 5 more rows of the data? ") # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
def main():
    while True:

   
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

        if restart.lower() == 'no':
            break

        elif restart.lower() != 'yes' or restart.lower() != 'no' :   
         restart= input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
         if restart.lower() == 'no':
            break
            
            
        


if __name__ == "__main__":
	main()
