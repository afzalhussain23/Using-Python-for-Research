from collections import Counter
def chance_homophily(chars):
    chars_counts = np.array(list(Counter(chars.values()).values()))
    chars_frequency = chars_counts / sum(chars_counts)
    return sum(chars_frequency**2)

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)

k = dict(Counter(favorite_colors))