---
layout: post
title: "Automatic dog bowl refill reminder"
description: "TL;DR: Use a leak sensor without an alarm to detect when water in a dog bowl drops below a certain level."
---

_**TL;DR:** Use a leak sensor without an alarm to detect when water in a dog bowl drops below a certain level._

Back in 2018, I installed an auto-refilling water bowl for our dog, mounting it on the wall in our laundry room. It worked well, but there was something disconcerting about having a water line under pressure, so when we moved to our new home, we didn’t take the auto-refilling bowl with us.

![Dog waterer in laundry room](/img/posts/2026-01-30-automatic-dog-bowl-refill-reminder/waterer.jpg)

Recently, after we had our second child, I found myself forgetting to fill our dog’s water bowl to his liking. As part of my never-ending quest to automate any need for my ability to remember anything, I looked into options for an automated reminder.

I happened upon a [Reddit post](https://www.reddit.com/r/homeassistant/comments/pddbea/dog_water_bowl_sensor/) showing a setup using an Aqara leak sensor with wires attached to the leads going into the bowl. From my research at the time, this was the only leak sensor I could find that _didn’t_ have a built-in alarm, which is important when being wet is the default state! 

At first, I tried to just install the sensor right inside the bowl, but I couldn’t find a way to keep it attached reliably and it got pretty gross with all of the dog slobber.

![Leak sensor installed in dog bowl](/img/posts/2026-01-30-automatic-dog-bowl-refill-reminder/sensor-in-bowl.jpg)

I ended up attaching it to the wall behind our dog bowls using a velcro Command strip and running a pair of twisted wires down to the bowl.

![Leak sensor installed above dog bowl](/img/posts/2026-01-30-automatic-dog-bowl-refill-reminder/sensor-above-bowl.jpg)

After about four months, the battery has depleted by about 25%. Not bad! But most importantly, our dog doesn't have to wait long for me to fill his bowl any more.
