# ##finding the ipl information


# import requests
# import pprint
# from bs4 import BeautifulSoup
# link = "https://www.iplt20.com/stats/2019"
# response = requests.get(link)
# soup = BeautifulSoup(response.text,"html.parser")
# table = soup.find("table",class_="standings-table standings-table--full")


# list_of_all_teams = []
# span_tags = table.find_all("span")
# count_of_span = 0
# for each_span in span_tags:
# 	count_of_span+=1
# 	dict_of_each_team = {}
# 	if count_of_span%2==0:
# 		dict_of_each_team["team_name"]=each_span.text
# 		list_of_all_teams.append(dict_of_each_team)

# #finding number of matches played
# tds = table.find_all("td",class_="standings-table__padded")
# td = set([i.text for i in tds])
# #finding the list
# for i in list_of_all_teams:
# 	for j in td:
# 		i["no_of_matches_played"] = j
# ##finding the no of matches won:- 
# trs = table.find_all("tr")
# count_of_tr=0
# big_list = []
# for i in trs:
# 	count_of_tr+=1
# 	if count_of_tr == 1:
# 		continue
# 	tds_related_to_option = i.find_all("td",class_="standings-table__optional")
# 	list_of_each_team = []
# 	for list_ in tds_related_to_option:
# 		list_of_each_team.append(list_.text)

# 	big_list.append(list_of_each_team)


# ##finding the total data

# list_for_remaining = []
# for i in big_list:
# 	count_of_j = 0
# 	dict_of_each_data = {}
# 	for j in i:
# 		count_of_j+=1
# 		if count_of_j == 1:
# 			dict_of_each_data["no-of_matches_won"] = j
# 		elif count_of_j == 2:
# 			dict_of_each_data["no_of_matches_lost"] = j
# 		elif count_of_j == 3:
# 			dict_of_each_data["no_of_matches_tied"] = j
# 	# print(dict_of_each_data)
# 	list_for_remaining.append(dict_of_each_data)

# for i in range(len(list_for_remaining)):
# 	for j,k in list_for_remaining[i].items():
# 		list_of_all_teams[i][j] = k

# ##finding the names of the movies:-
# list_team_names =[]
# trs = table.find_all("a")
# for i in trs:
# 	span = i.find("span").text
# 	list_team_names.append(span)
# # print(list_team_names)

# ##finding the total dictionery:-
# total_dictionery = {}
# for i in range(len(list_of_all_teams)):
# 	total_dictionery[list_team_names[i]]=list_of_all_teams[i]
# pprint.pprint(total_dictionery)