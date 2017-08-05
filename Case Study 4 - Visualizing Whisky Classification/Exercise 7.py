region_cols = [region_colors[i] for i in list(whisky["Region"])]
classification_cols = [cluster_colors[i] for i in list(whisky["Group"])]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)