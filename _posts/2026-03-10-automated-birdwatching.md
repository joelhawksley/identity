---
layout: post
title: Automatic bird identification with Home Assistant
description: "I use Birdnet-Go to identify bird calls using the audio from my Ubiquiti cameras, displaying the most interesting bird detected in the past day on my Timeframe displays:"
image: /img/posts/2026-03-10-automated-birdwatching/most-interesting.jpg
---

{% include figure.html src="/img/posts/2026-03-10-automated-birdwatching/most-interesting.jpg" alt="Close-up image of an e-paper display with text saying 'Barred Owl'." caption="A Barred Owl detected by BirdNET-Go" %}

My wife and I love birding. Our interest in the hobby intensified during COVID, spending many mornings at our [favorite birdwatching spot](https://bouldercounty.gov/open-space/parks-and-trails/walden-ponds-wildlife-habitat/).

When [Merlin Bird ID](https://merlin.allaboutbirds.org/) added [Sound ID](https://merlin.allaboutbirds.org/sound-id/) in 2021, we were hooked immediately! It felt like something out of Harry Potter to be able to have our phones tell us what bird we were hearing, even if we couldn’t see it. About a year later, the [BirdNET-Pi](https://github.com/mcguirepr89/BirdNET-Pi) project made it easy to run the Sound ID model locally. One of the audio sources supported was the RTSP output, which I used with two of our Ubiquiti cameras. 

While it worked well at identifying birds accurately, the app crashed randomly. First, I tried installing BirdNET-Pi as a Home Assistant Addon, as my HA hardware was vastly overprovisioned compared to the Raspberry Pi. This reduced the crashes, but did not eliminate them. A few months later, a fellow birding and Home Assistant enthusiast recommended I try [BirdNET-Go](https://github.com/tphakala/birdnet-go), which is a rewrite of BirdNET-Pi with improved stability and performance. This fixed the reliability issues once and for all and I haven’t had any crashes since then.

## Sifting through the data

With the stability issue resolved, I had a bigger problem: what to do with all of this data? While BirdNET-Go provided a nice dashboard for viewing detections, I wanted to find a way to surface insights about the data that were interesting to me without having to comb through the feed. Around the same time, I was developing the latest version of [Timeframe](/2026/02/17/timeframe.html), my e-paper dashboard system. Caitlin suggested we highlight the most interesting detection of the past day. 

After trying a few different algorithms, I ended up with a simple REST sensor. The sensor fetches the summary data from BirdNET-Go, filters it to only include detections from the past day, then sorts them by the bird most recently heard for the first time:

{% raw %}
```yml
# configuration.yaml
sensor:
  - platform: rest
    resource: http://homeassistant.local:8080/api/v2/analytics/species/summary
    scan_interval: 300
    name: "Most Interesting Bird"
    unique_id: birdnet_most_interesting
    value_template: >
      {% set cutoff = (now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S') %}
      {% set birds = value_json
        | rejectattr('common_name', 'eq', 'Engine')
        | selectattr('last_heard', 'ge', cutoff)
        | sort(attribute='first_heard', reverse=true)
        | list %}
      {{ birds[0].common_name if birds | length > 0 else 'Unknown' }}
```
{% endraw %}

It’s been fun to see new species appear for the first time as an early spring arrives here in Colorado:

{% include figure.html src="/img/posts/2026-03-10-automated-birdwatching/detections.png" alt="A timeline view of the sensor's value showing it changing from Black-capped Chickadee to Western Bluebird to Say's Phoebe" caption="Three new species in two days!" %}