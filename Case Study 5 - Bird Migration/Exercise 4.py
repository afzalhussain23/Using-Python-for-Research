grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_speeds = grouped_birdday.speed_2d.mean()


eric_daily_speed  = mean_speeds["Eric"]
sanne_daily_speed = mean_speeds["Sanne"]
nico_daily_speed  = mean_speeds["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()