"""
@author: Aswatth
"""
import streamlit as st
import pandas as pd
import os

def RemoveDuplicate(listToRemoveDuplicates):
    return list(set(listToRemoveDuplicates))

def TossTab(matchDataFrame):
    #Get venue list
    venueList = matchDataFrame['Venue']
    #Removing duplicates
    venueList = RemoveDuplicate(venueList)

    #Get team list
    teamList = matchDataFrame['Team1']
    #Remove duplicates
    teamList = RemoveDuplicate(teamList)

    #Get season list
    seasonList = matchDataFrame['Season']
    #Removin duplicates
    seasonList = RemoveDuplicate(seasonList)
    
    st.markdown(os.getcwd())
    ##### Venue data calculation #####
    #st.dataframe(matchDataFrame)
    selectedVenue = st.selectbox('Venue',venueList)
    
    venue_subset = matchDataFrame[matchDataFrame['Venue'] == selectedVenue]

    total_games = len(venue_subset)
    toss_outcome = venue_subset[ venue_subset ["TossWinner"]== venue_subset["WinningTeam"] ] 
    toss_winners = len(toss_outcome)

    TossAndMatchWin_Percentage = toss_winners / total_games * 100
    TossWinAndFieldWin_Percentage = len(venue_subset [venue_subset["TossDecision"]=='field']) / total_games * 100

    # st.dataframe(venue_subset)
    st.markdown('In **'+ selectedVenue +'**:')
    st.markdown('Percentage of chances when team won the toss and match: '+ str(round(TossAndMatchWin_Percentage,2)) + '%')
    st.markdown('Percentage of chances when team chose to field: '+ str(round(TossWinAndFieldWin_Percentage,2)) + '%')
    # st.markdown('Matches won by **'+ selectedTeam2 +'** when they won the toss: '+str(41)+'%') #TODO: To be updated with calculated number
    # st.markdown('Time when **'+ selectedTeam1 +'** who won the toss and chose to bat: '+str(42)+'%') #TODO: To be updated with calculated number
    # st.markdown('Time when **'+ selectedTeam2 +'** who won the toss and chose to bat: '+str(42)+'%') #TODO: To be updated with calculated number

    ##### Season data calculation#####    
    selectedSeason = st.selectbox('Season', seasonList)
    season_subset = matchDataFrame[matchDataFrame['Season'] == selectedSeason]

    total_games = len(season_subset)

    season_trends = len(season_subset[ season_subset ["TossWinner"] == season_subset["WinningTeam"] ])
    TossAndMatchWin_Percentage = season_trends / total_games * 100
    TossWinAndFieldWin_Percentage = len(season_subset [season_subset["TossDecision"] =='field']) / total_games * 100

    st.markdown('In **'+ str(selectedSeason) +'**:')
    st.markdown('Percentage of chances when team won the toss and match: '+ str(round(TossAndMatchWin_Percentage,2)) + '%')
    st.markdown('Percentage of chances when team chose to field: '+ str(round(TossWinAndFieldWin_Percentage,2)) + '%')

    ##### Team data calculation #####
    selectedTeam1 = st.selectbox('Team 1',teamList)

    team_trends = matchDataFrame [ matchDataFrame ["Team1"] == selectedTeam1]
    team_trends2 = matchDataFrame [ matchDataFrame["Team2"] == selectedTeam1] 

    total = len(team_trends) + len(team_trends2)

    team = len(team_trends[ team_trends ["TossWinner"] == selectedTeam1])
    team = team + len(team_trends2 [team_trends2 ["TossWinner"] == selectedTeam1])

    total_toss_wins = team 
    toss_win_percentage = total_toss_wins / total * 100
    st.markdown(selectedTeam1 + ' won the toss ' + str(round(toss_win_percentage,2)) + '% of the time')

    team1 = team_trends[ team_trends ["TossWinner"] == selectedTeam1]
    team2 = team_trends2 [team_trends2 ["TossWinner"] == selectedTeam1]

    team_wins = len(team1 [team1 ["WinningTeam"] == selectedTeam1]) + len(team2 [team2 ["WinningTeam"] == selectedTeam1])

    match_win_percentage = team_wins / total_toss_wins * 100

    st.markdown(selectedTeam1 + ' won the match ' + str(round(match_win_percentage,2)) + '% of the time when they won toss')
    
    ##### Opposition Data calculation #####
    oppositionTeam = st.selectbox('Team 2',teamList)
    team_trends = matchDataFrame [ matchDataFrame ["Team1"] == oppositionTeam]
    team_wins_bat = len(team_trends [ team_trends[ "WinningTeam"] == oppositionTeam])

    team_trends2 = matchDataFrame [ matchDataFrame ["Team2"] == oppositionTeam]
    team_wins_bowl = len(team_trends [ team_trends[ "WinningTeam"] == oppositionTeam])

    total = team_wins_bat + team_wins_bowl

    bat_win_percentage = team_wins_bat / total * 100
    bowl_win_percentage = team_wins_bowl / total * 100

    st.markdown('Percentage of wins when '+ oppositionTeam + ' chose to bat: ' + str(round(bat_win_percentage,2)))
    st.markdown('Percentage of wins when '+ oppositionTeam + ' chose to bowl: ' + str(round(bowl_win_percentage,2)))

def BatterInfo(matchDataFrame ,statsDataFrame):
    #Get list of Venues
    venueList = matchDataFrame['venue']
    #Removing duplicates
    venueList = RemoveDuplicate(venueList)

    #Get list of batsmen
    listOfBatsmen = statsDataFrame['batsman'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBatsmen = RemoveDuplicate(listOfBatsmen)

    #Get list of teams
    teamList = matchDataFrame['team1']
    #Remove duplicates
    teamList = RemoveDuplicate(teamList)

    st.selectbox('Batsmen',listOfBatsmen,key='batter_venue')
    st.selectbox('Venue',venueList,key='venue_batter')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

    st.selectbox('Batsmen',listOfBatsmen,key='batter_team')
    st.selectbox('Opposition Team',teamList,key='team_batter')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

def BowlerInfo(matchDataFrame ,statsDataFrame):
    #Get list of Venues
    venueList = matchDataFrame['venue']
    #Removing duplicates
    venueList = RemoveDuplicate(venueList)

    #Get list of bowlers
    listOfBowler = statsDataFrame['bowler'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBowler = RemoveDuplicate(listOfBowler)

    #Get list of teams
    teamList = matchDataFrame['team1']
    #Remove duplicates
    teamList = RemoveDuplicate(teamList)

    st.selectbox('Bowler',listOfBowler,key='bowler_venue')
    st.selectbox('Venue',venueList,key='venue_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

    st.selectbox('Bowler',listOfBowler,key='bowler_team')
    st.selectbox('Opposition Team',teamList,key='team_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data

def BatterVsBowler(matchDataFrame ,statsDataFrame):
    #Get list of batsmen
    listOfBatsmen = statsDataFrame['batsman'] #TODO: To be updated based on selected team
    #Remove duplicates
    listOfBatsmen = RemoveDuplicate(listOfBatsmen)

    #Get list of teams
    teamList = matchDataFrame['team1']
    #Remove duplicates
    teamList = RemoveDuplicate(teamList)

    st.selectbox('Batsmen',listOfBatsmen,key='batter_bowler')
    st.selectbox('Opposition Team',teamList,key='team_batter_bowler')
    st.dataframe([1,2,3]) #TODO: To be updated based on calculated data  

currentPath = os.getcwd()
dataPath = currentPath.replace(r'\StreamLit', r'\archive\IPL_Matches_2008_2022.csv')
matchDataFrame = pd.read_csv(dataPath)
#matchStatsDataFrame = pd.read_csv(r'C:\Users\<USER-NAME>\Desktop\fantasyer\archive\deliveries.csv')

tossTab, batterInfo, bowlerInfo, batterVsBowler = st.tabs(['Toss', 'BatterInfo', 'BowlerInfo', 'Batter vs Bowler'])

with tossTab:
    TossTab(matchDataFrame)

# with batterInfo:
#     BatterInfo(matchDataFrame, matchStatsDataFrame)

# with bowlerInfo:
#     BowlerInfo(matchDataFrame, matchStatsDataFrame)

# with batterVsBowler:
#     BatterVsBowler(matchDataFrame, matchStatsDataFrame)
