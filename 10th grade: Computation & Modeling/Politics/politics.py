# study: https://towardsdatascience.com/how-statistically-biased-is-our-news-f28f0fab3cb3

find_info_on = []
find_info_on_all = False

print_all_names = False
print_classifications = False
print_observations = False # so far, just averages

min_reliability = 50
find_reliable = ['more_conservative']
# find_bias (not coded)

make_plot = False

"""

Common sources:
- AP
- CNN
- FoxNews
- MSNBC
- NewYorkPost
- NewYorkTimes
- NewsMax
- OneAmericaNewsNetwork
- Politico
- Reuters
- Vox
- WallStreetJournal
- WashingtonPost
- WashingtonTimes

Reliability:
- Measured on a scale from 0 to 64
- The highest value is only 51.98 (81.2%)
- Values from 0 to 16 (0% to 25%): extremely unreliable (literal fake news)
- Values from 16 to 24 (25% to 37.5%): very questionable content
- Values from 24 to 46 (37.5% to 71.875%): reliable but may have a lot of opinions
- Values from 46-64 (71.875% - 100%): most reliable for factual news

Bias:
- Measured on a scale from -42 to +42
- Values from -42 to -18 (-100% to -42.86%): extremely biased towards the left
- Values from -18 to -6 (-42.86% to -14.29%): moderately biased towards the left
- Values from -6 to -3 (-14.29% to -7.14%): slightly biased towards the left
- Values from -3 to +3 (-7.14% to 7.14%): neutral
- Values from +3 to +6 (7.14% to 14.29%): slightly biased towards the right
- Values from +6 to +18 (14.29% to 42.86%): moderately biased towards the right
- Values from +18 to +42 (42.86% to 100%): extremely biased towards the right

"""

# code stuff
########################################################

all_sources = []
def converter(string):
    better_string = ''
    for char in string:
        if char != '' and char != ' ':
            better_string += char
    better_string_list = better_string.split('|')[1:4]
    all_sources.append(better_string_list)

# sources
if True:
 converter('| ABC news                  |       49.47 |  -1.85 |')
 converter('| Al Jazeera                |       49.47 |  -3.71 |')
 converter('| Alternet                  |        21.4 | -19.16 |')
 converter('| American Thinker          |        23.1 |  29.82 |')
 converter('| AP                        |       51.98 |  -1.06 |')
 converter('| Axios                     |       47.36 |  -5.74 |')
 converter('| BBC                       |       46.56 |  -3.03 |')
 converter('| Bipartisan Report         |       19.29 | -23.55 |')
 converter('| Bloomberg                 |       47.63 |  -0.85 |')
 converter('| Breitbart                 |       20.58 |  22.57 |')
 converter('| Business Insider          |       43.13 |  -0.38 |')
 converter('| BuzzFeed                  |        43.2 |  -7.06 |')
 converter('| CBS                       |       47.06 |  -1.85 |')
 converter('| Christian Science Monitor |       44.47 |  -0.21 |')
 converter('| CNN                       |       42.22 |  -5.69 |')
 converter('| Conservative Review       |        21.8 |   25.3 |')
 converter('| Conservative Tribune      |       29.69 |  17.22 |')
 converter('| Counterpunch              |       25.06 | -19.38 |')
 converter('| Crooks and Liars          |       23.06 | -23.46 |')
 converter('| Daily Beast               |       34.44 | -16.25 |')
 converter('| Daily Caller              |       23.93 |  20.06 |')
 converter('| Daily Kos                 |       23.16 | -21.49 |')
 converter('| Daily Mail                |       30.36 |   3.27 |')
 converter('| Daily Signal              |       24.79 |  23.31 |')
 converter('| Daily Wire                |       24.39 |  16.35 |')
 converter('| Democracy Now             |       32.91 | -19.31 |')
 converter('| Financial Times           |       46.71 |   0.62 |')
 converter('| Fiscal Times              |       44.72 |   1.52 |')
 converter('| Forbes                    |       40.27 |    0.2 |')
 converter('| Foreign Policy            |       41.49 |  -1.65 |')
 converter('| Fortune                   |       45.15 |   0.43 |')
 converter('| Forward                   |       37.57 |  -5.69 |')
 converter('| Fox News                  |       26.76 |  15.31 |')
 converter('| FreeSpeech TV             |       24.77 | -22.49 |')
 converter('| Huffington Post           |       39.98 | -11.64 |')
 converter('| IJR                       |          44 |   6.73 |')
 converter('| InfoWars                  |       12.97 |  31.05 |')
 converter('| Intercept                 |       37.76 | -15.52 |')
 converter('| Jacobin                   |       32.32 | -19.92 |')
 converter('| LA Times                  |       48.88 |  -3.06 |')
 converter('| Life News                 |       24.49 |  24.75 |')
 converter('| Marketwatch               |        44.8 |  -0.54 |')
 converter('| Mother Jones              |       37.31 | -13.92 |')
 converter('| MSNBC                     |       46.39 |  -6.11 |')
 converter('| National Enquirer         |        9.65 |   5.41 |')
 converter('| National Public Radio     |        49.9 |  -2.73 |')
 converter('| National Review           |       26.36 |  16.23 |')
 converter('| New Republic              |       36.43 | -12.82 |')
 converter('| New York Post             |        38.7 |   5.15 |')
 converter('| New York Times            |        47.5 |  -4.01 |')
 converter('| News and Guts             |       34.98 |  -9.84 |')
 converter('| NewsMax                   |       33.15 |  13.61 |')
 converter('| NewsPunch                 |       14.39 |  28.58 |')
 converter('| Newsy                     |        42.1 |     -8 |')
 converter('| Occupy Democrats          |          20 | -25.59 |')
 converter('| One America News Network  |       30.57 |  15.89 |')
 converter('| OZY                       |       40.99 |  -5.43 |')
 converter('| Palmer Report             |       17.66 | -29.37 |')
 converter('| PBS                       |       47.86 |  -2.37 |')
 converter('| PJ Media                  |       18.36 |  20.33 |')
 converter('| Politico                  |       46.11 |  -5.24 |')
 converter('| ProPublica                |       47.78 |  -5.93 |')
 converter('| Quartz                    |       41.34 |  -3.89 |')
 converter('| Reason                    |       38.27 |   4.12 |')
 converter('| RedState                  |       26.44 |  20.08 |')
 converter('| Reuters                   |       51.64 |  -0.95 |')
 converter('| Second Nexus              |       24.29 | -22.61 |')
 converter('| ShareBlue                 |       22.71 | -24.95 |')
 converter('| Slate                     |       31.12 | -18.47 |')
 converter('| Talking Points Memo       |       41.96 |  -5.67 |')
 converter('| The Advocate              |       49.47 |  -1.85 |')
 converter('| The American Conservative |       28.65 |  10.82 |')
 converter('| The American Spectator    |          22 |  23.89 |')
 converter('| The Atlantic              |       40.16 |  -6.41 |')
 converter('| The Blaze                 |       27.34 |   15.7 |')
 converter('| The Economist             |       42.34 |  -2.43 |')
 converter('| The Federalist            |       22.23 |  23.29 |')
 converter('| The Gateway Pundit        |       12.44 |  28.55 |')
 converter('| The Guardian              |       47.66 |  -6.45 |')
 converter('| The Hill                  |       46.23 |   0.09 |')
 converter('| The Nation                |       33.39 | -16.89 |')
 converter('| The New Yorker            |       41.85 |   -6.9 |')
 converter('| The Progressive           |       37.79 | -17.48 |')
 converter('| The Skimm                 |       41.67 |  -3.31 |')
 converter('| The Week                  |       30.98 |  -8.31 |')
 converter('| Think Progress            |       35.59 | -19.12 |')
 converter('| Time                      |        42.7 |  -4.35 |')
 converter('| Truthout                  |       24.07 |  -24.4 |')
 converter('| Twitchy                   |       17.08 |  20.57 |')
 converter('| USA Today                 |       46.07 |  -2.03 |')
 converter('| Vanity Fair               |       35.42 | -17.98 |')
 converter('| Vox                       |       41.97 |  -8.75 |')
 converter('| Wall Street Journal       |       48.33 |   1.89 |')
 converter('| Washington Examiner       |       29.07 |  12.17 |')
 converter('| Washington Free Beacon    |       35.07 |  16.71 |')
 converter('| Washington Monthly        |       26.91 | -14.68 |')
 converter('| Washington Post           |       43.73 |  -4.18 |')
 converter('| Washington Times          |       31.34 |  12.97 |')
 converter('| Weather.com               |       51.55 |  -2.43 |')
 converter('| Wonkette                  |       15.27 | -31.15 |')
 converter('| World Truth TV            |        7.41 |   8.48 |')
 converter('| WorldNetDaily             |       16.95 |  22.92 |')

def convert_all_sources_dict():
    all_sources_dict = []
    
    for source in all_sources:
        
        name = source[0]
        reliability = float(source[1]) # 0 to 64
        reliability_percent = round(100 * reliability / 64, 2) # 0 to 100
        
        if reliability < 16:
            reliability_classification = 'extremely unreliable'
        elif reliability < 24:
            reliability_classification = 'very questionable content'
        elif reliability < 46:
            reliability_classification = 'reliable but may have a lot of opinions'
        else:
            reliability_classification = 'most reliable for factual news'
        
        bias = float(source[2]) # -42 to +42
        bias_percent = round(100 * float(bias) / 42, 2) # 0 to 100
        
        if bias < -18:
            bias_classification = 'extremely biased towards the left'
        elif bias < -6:
            bias_classification = 'moderately biased towards the left'
        elif bias < -3:
            bias_classification = 'slightly biased towards the left'
        elif bias < 3:
            bias_classification = 'neutral'
        elif bias < 6:
            bias_classification = 'slightly biased towards the right'
        elif bias < 18:
            bias_classification = 'moderately biased towards the right'
        else:
            bias_classification = 'extremely biased towards the right'
        
        source_dict = {
            'name': name,
            # 'reliability': reliability, (doesnt work rn)
            'reliability': reliability_percent,
            'reliability_classification': reliability_classification,
            # 'bias': bias, (doesnt work rn)
            'bias': bias_percent,
            'bias_classification': bias_classification
        }

        all_sources_dict.append(source_dict)
    
    return all_sources_dict

all_sources_info = convert_all_sources_dict()

def report(source_name):
    
    correct_source = 0
    for source in all_sources_info:
        if source['name'] == source_name:
            correct_source = source
    
    if correct_source == 0:
        print("\ncould not find a source for " + source_name)
    
    print("\nName: {}".format(correct_source['name']))
    
    print("reliability: {}".format(correct_source['reliability']))
    
    if print_classifications:
        print("reliability_classification: {}".format(correct_source['reliability_classification']))
    
    print("bias: {}".format(correct_source['bias']))
    
    if print_classifications:
        print("bias_classification: {}".format(correct_source['bias_classification']))

def find_average(category, condition_function, print_word):
    
    related_sources = []
    for source in all_sources_info:
        if condition_function(source):
            related_sources.append(source)
    
    if category == 'reliability':
        average_reliability = True
    elif category == 'bias':
        average_reliability = True
    elif category == 'both':
        average_reliability = True
        average_bias = True
    else:
        return 'not a valid category'
    
    average = {'name': 'n/a', 'reliability': 0, 'bias': 0}
    for source in related_sources:
        if average_reliability:
            average['reliability'] += source['reliability']
        if average_bias:
            average['bias'] += source['bias']
    average['reliability'] /= len(related_sources)
    average['bias'] /= len(related_sources)

    print('\nAverage of {}:'.format(print_word))
    for (key, value) in average.items():
        if key != 'name':
            print('{}:'.format(key), round(value, 3))
    
if find_info_on_all:
    for source in all_sources_info:
        name = source['name']
        report(name)
else:
    for name in find_info_on:
        report(name)

if print_all_names:
    for source in all_sources_info:
        print(source['name'])

if print_observations:
    find_average('both', lambda x : x['bias'] < -18, 'extremely biased towards the left')
    find_average('both', lambda x : x['bias'] < -6, 'moderately biased towards the left')
    find_average('both', lambda x : x['bias'] > -6 and x['bias'] < 6, 'neutral')
    find_average('both', lambda x : x['bias'] > 6, 'moderately biased towards the right')
    find_average('both', lambda x : x['bias'] > 18, 'extremely biased towards the right')

if make_plot:

    import matplotlib.pyplot as plt
    plt.style.use('bmh')
    
    colors = ['#00d0ff', '#0000ff', '#000000', '#ff0000', '#8b0000']

    biases_range = [[], [], [], [], []]
    reliabilities_range = [[], [], [], [], []]

    for source in all_sources_info:
        
        bias = source['bias']
        reliability = source['reliability']
        
        if bias < -18:
            biases_range[0].append(bias)
            reliabilities_range[0].append(reliability)
        elif bias < -6:
            biases_range[1].append(bias)
            reliabilities_range[1].append(reliability)
        elif bias < 6:
            biases_range[2].append(bias)
            reliabilities_range[2].append(reliability)
        elif bias < 18:
            biases_range[3].append(bias)
            reliabilities_range[3].append(reliability)
        else:
            biases_range[4].append(bias)
            reliabilities_range[4].append(reliability)

    progressive = plt.scatter(biases_range[0], reliabilities_range[0], marker='o', color=colors[0])
    liberal = plt.scatter(biases_range[1], reliabilities_range[1], marker='o', color=colors[1])
    neutral = plt.scatter(biases_range[2], reliabilities_range[2], marker='o', color=colors[2])
    conservative = plt.scatter(biases_range[3], reliabilities_range[3], marker='o', color=colors[3])
    more_conservative = plt.scatter(biases_range[4], reliabilities_range[4], marker='o', color=colors[4])

    plt.legend((progressive, liberal, neutral, conservative, more_conservative),
           ('progressive', 'liberal', 'neutral', 'conservative', 'more conservative'),
           scatterpoints=1,
           loc='upper right')

    plt.xlabel('Bias')
    plt.ylabel('Reliability')
    plt.title('Bias vs. Reliability')
    plt.savefig('politics.png')

if find_reliable == ['all']:
    find_reliable = ['progressive', 'liberal', 'neutral', 'conservative', 'more_conservative']

for leaning in find_reliable:

    reliable_progressive = []
    reliable_liberal = []
    reliable_neutral = []
    reliable_conservative = []
    reliable_more_conservative = []

    for source in all_sources_info:
        source_bias = source['bias']
        source_reliability = source['reliability']

        if source['reliability'] > min_reliability:
            
            if source_bias < -18:
                reliable_progressive.append(source['name'])
            elif source_bias < -6:
                reliable_liberal.append(source['name'])
            elif source_bias < 6:
                reliable_neutral.append(source['name'])
            elif source_bias < 18:
                reliable_conservative.append(source['name'])
            else:
                reliable_more_conservative.append(source['name'])
    
    if leaning == 'progressive':
        print("\nreliable_progressive:", reliable_progressive)
    elif leaning == 'liberal':
        print("\nreliable_liberal:", reliable_liberal)
    elif leaning == 'neutral':
        print("\nreliable_neutral:", reliable_neutral)
    elif leaning == 'conservative':
        print("\nreliable_conservative:", reliable_conservative)
    elif leaning == 'more_conservative':
        print("\nreliable_more_conservative:", reliable_more_conservative)