---
layout: post
title: "Home Assistant video call status light"
description: “TL;DR:** Use the Home Assistant MacOS app to control smart lights based on video call status.”
---

<video autoplay muted loop playsinline controls style="width:100%">
  <source src="/img/posts/2026-02-05-home-assistant-video-call-status-light/office-call-light-720.mp4" type="video/mp4">
</video>

_**TL;DR:** Use the Home Assistant MacOS app to control smart lights based on video call status._

In order to focus completely on my work, I often wear noise cancelling headphones, making it difficult to hear a knock on the door. I’m also in meetings quite a bit, when a door knock is less welcome. While I try to keep my calendar up to date so my wife knows when I’m on a call, I’ll occasionally have ad-hoc conversations for pairing, etc.

I recently set up a system to indicate whether I am listening to music or on a video call, using Zigbee night lights from Third Reality, one in the hallway outside my office door and another inside the door in my office so I can know what the hallway light is set to.

In Home Assistant, I created a helper called `Office audio state` returning `input`, `output`, or `off` using sensor data from the Home Assistant app running on my personal and work laptops (be sure to replace the sensor names with yours):

```yaml
{\% if states("binary_sensor.joelhawksley_audio_input_in_use_2") == "on" or states("binary_sensor.joel_audio_input_in_use") == "on" \%}
input
{\% elif states("binary_sensor.joelhawksley_audio_output_in_use_2") == "on" or states("binary_sensor.joely_audio_output_in_use") == "on" \%}
output
{\% else \%}
off
{\% endif \%}
```

I then have an automation listening to changes to the helper (debounced for 5 seconds to avoid false triggers from momentary changes) and switching between scenes on the lights (blue for video call, yellow for listening, off otherwise):

```yaml
alias: OFFICE Hallway nightlight audio input indication
description: ""
triggers:
  - trigger: state
    entity_id:
      - sensor.joelhawksley_audio_state
    for:
      hours: 0
      minutes: 0
      seconds: 5
conditions: []
actions:
  - if:
      - condition: state
        entity_id: sensor.joelhawksley_audio_state
        state:
          - input
    then:
      - action: scene.turn_on
        metadata: {}
        data: {}
        target:
          entity_id: scene.upstairs_hallway_night_light_blue
    else:
      - if:
          - condition: state
            entity_id: sensor.joelhawksley_audio_state
            state:
              - output
        then:
          - action: scene.turn_on
            metadata: {}
            data: {}
            target:
              entity_id: scene.upstairs_hallway_night_light_yellow
        else:
          - type: turn_off
            device_id: 3dc9a44855f7e46888f1c137990de9a8
            entity_id: 068da579d67f52febf9b5e19a09841e1
            domain: light
          - type: turn_off
            device_id: 77b1714316849f1f830c7b7744010682
            entity_id: 46e8791366840c4c8038c1e6edeff267
            domain: light
mode: single
```

As a bonus, the night lights also serve as Zigbee routers, extending the range and stability of our Zigbee network!
