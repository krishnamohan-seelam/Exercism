from collections import defaultdict

def tally(tournament_results):

    if not tournament_results:
        return 'Team                           | MP |  W |  D |  L |  P'

    teams = defaultdict(list)
    tournaments_split = tournament_results.split('\n')
    for tournament in tournaments_split:
        team_x,team_y,result = tournament.split(';')
        if result == 'draw':
            teams[team_x].append('draw')
            teams[team_y].append('draw')
        elif result == 'win':
            teams[team_x].append('win')
            teams[team_y].append('loss')
        elif result == 'loss':
            teams[team_x].append('loss')
            teams[team_y].append('win')
        
    team_standings= defaultdict(dict)
    for team in teams:
        result = teams[team]
        team_standings[team] ={ 'MP':len(result),'win': result.count('win'),
                                'draw':result.count('draw'),'loss':result.count('loss'),
                                'P':result.count('win') * 3 + result.count('draw') * 1
                              }
    points_table =sorted(team_standings.items(), key=lambda s: (s[1]['P']*-1,s[0]), reverse=False)
    team_standings = []
    for team ,stats in points_table:
        team_standing ="{0:<31}| {1:>2s} | {2:>2s} | {3:>2s} | {4:>2s} | {5:>2s}\n".format(
                        team,
                        str(stats['MP']),
                        str(stats['win']),
                        str(stats['draw']),
                        str(stats['loss']),
                        str(stats['P'])
                        )
        team_standings.append(team_standing)
    team_standings[-1] = team_standings[-1].rstrip()

    return 'Team                           | MP |  W |  D |  L |  P\n'+"".join(team_standings) 
        



