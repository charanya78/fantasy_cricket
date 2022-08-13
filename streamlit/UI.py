"""
@author: Aswatth
"""
import streamlit as st
import pandas as pd

def RemoveDuplicate(listToRemoveDuplicates):
    return list(set(listToRemoveDuplicates))

def TossTab(matchDataFrame):
    #Get list of stadiums
    listOfStadiums = matchDataFrame['venue']
    #Removing duplicates
    listOfStadiums = RemoveDuplicate(listOfStadiums)

    #Get list of teams
    listOfTeams = matchDataFrame['team1']
    #Remove duplicates
    listOfTeams = RemoveDuplicate(listOfTeams)

    #st.dataframe(matchDataFrame)
    selectedTeam1 = st.selectbox('Team 1',listOfTeams)
    selectedTeam2 = st.selectbox('Team 2',listOfTeams)
    selectedStadium = st.selectbox('Venue',listOfStadiums)

    st.markdown('In **'+ selectedStadium +'**:')
    st.markdown('Matches won by **'+ selectedTeam1 +'** when they won the toss: '+str(41)+'%') #TODO: To be updated with calculated number
    st.markdown('Matches won by **'+ selectedTeam2 +'** when they won the toss: '+str(41)+'%') #TODO: To be updated with calculated number
    st.markdown('Time when **'+ selectedTeam1 +'** who won the toss and chose to bat: '+str(42)+'%') #TODO: To be updated with calculated number
    st.markdown('Time when **'+ selectedTeam2 +'** who won the toss and chose to bat: '+str(42)+'%') #TODO: To be updated with calculated number

def BatterInfo(matchDataFrame ,statsDataFrame):
    #Get list of stadiums
    listOfStadiums = matchDataFrame['venue']
    #Removing duplicates
    listOfStadiums = RemoveDuplicate(listOfStadiums)

    #Get list of batsmen
    listOfBatsmen = statsDataFrame['batsman'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBatsmen = RemoveDuplicate(listOfBatsmen)

    #Get list of teams
    listOfTeams = matchDataFrame['team1']
    #Remove duplicates
    listOfTeams = RemoveDuplicate(listOfTeams)

    st.selectbox('Batsmen',listOfBatsmen,key='batter_venue')
    st.selectbox('Venue',listOfStadiums,key='venue_batter')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

    st.selectbox('Batsmen',listOfBatsmen,key='batter_team')
    st.selectbox('Opposition Team',listOfTeams,key='team_batter')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

def BowlerInfo(matchDataFrame ,statsDataFrame):
    #Get list of stadiums
    listOfStadiums = matchDataFrame['venue']
    #Removing duplicates
    listOfStadiums = RemoveDuplicate(listOfStadiums)

    #Get list of bowlers
    listOfBowler = statsDataFrame['bowler'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBowler = RemoveDuplicate(listOfBowler)

    #Get list of teams
    listOfTeams = matchDataFrame['team1']
    #Remove duplicates
    listOfTeams = RemoveDuplicate(listOfTeams)

    st.selectbox('Bowler',listOfBowler,key='bowler_venue')
    st.selectbox('Venue',listOfStadiums,key='venue_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

    st.selectbox('Bowler',listOfBowler,key='bowler_team')
    st.selectbox('Opposition Team',listOfTeams,key='team_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

def BatterVsBowler(matchDataFrame ,statsDataFrame):
    #Get list of batsmen
    listOfBatsmen = statsDataFrame['batsman'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBatsmen = RemoveDuplicate(listOfBatsmen)

    #Get list of teams
    listOfTeams = matchDataFrame['team1']
    #Remove duplicates
    listOfTeams = RemoveDuplicate(listOfTeams)

    st.selectbox('Batsmen',listOfBatsmen,key='batter_bowler')
    st.selectbox('Opposition Team',listOfTeams,key='team_batter_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data  

matchDataFrame = pd.read_csv(r'C:\Users\Aswatth\Desktop\fantasy_cricket\archive\matches.csv')
matchStatsDataFrame = pd.read_csv(r'C:\Users\Aswatth\Desktop\fantasy_cricket\archive\deliveries.csv')

tossTab, batterInfo, bowlerInfo, batterVsBowler = st.tabs(['Toss', 'BatterInfo', 'BowlerInfo', 'Batter vs Bowler'])

with tossTab:
    TossTab(matchDataFrame)

with batterInfo:
    BatterInfo(matchDataFrame, matchStatsDataFrame)

with bowlerInfo:
    BowlerInfo(matchDataFrame, matchStatsDataFrame)

with batterVsBowler:
    BatterVsBowler(matchDataFrame, matchStatsDataFrame)