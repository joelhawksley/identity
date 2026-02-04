---
layout: post
title: My Ubiquiti Unifi Protect bird nest camera setup
excerpt: Open up a Unifi G5 Bullet camera to adjust the manual focus distance for usage in close quarters, such as a bird nest.
---

<video controls>
  <source width="320" height="240" src="/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/nest_redo.mp4" type="video/mp4">
</video>

### TL;DR

Open up a [Unifi G5 Bullet](https://store.ui.com/us/en/products/uvc-g5-bullet) camera to adjust the manual focus distance for usage in close quarters, such as a bird nest.

### Background

Before our house burned down in the Marshall Fire, we had a few families of house finches that nested in the pine tree outside of my office window. Their comings and goings were a nice form of entertainment while working from home. 

During the process of rebuilding our home, the finches took up residence in our framed-out house in the spring, raising a few clutches. Once the building was closed in, we wondered where they would nest, as our neighborhood lost most of its trees in the fire.

As the finishing touches went on the house, we realized that we were creating the perfect nesting spots in the hollowed-out tops of the craftsman-style pre-fabricated corbels under our roof gables, of which there are about 20 on our home. On most of of them, the top was exposed:

![Corbels on the side of a house](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/corbels.jpg)

While we didn't want to deter all nesting, we had our builder close off all but the four that sit above windows on the main floor of the house. And sure enough, we were right! The finches took up the new spot with much delight, nesting in two of the four last spring.

### Setting up a nest camera

Unfortunately the nests were basically impossible to observe, which I'm sure the finches appreciated. We wanted to give them their space but still be able to see the action, so I looked into setting up a camera for one of the nesting spots.

After some research, I found that none of the Ubiquiti cameras would focus as close as I needed (~1ft). Luckily, a helpful poster on the Ubiquiti forums noted that the Bullet cameras can be manually focused if you're willing to void your warranty.

Here is how the camera focus looked straight out of the box:

![The unfocused view from the camera](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/camera-unfocused.jpg)

Not even close. In most applications, a hyperfocal approach is likely preferred, so I'm guessing the out-of-box focus distance is around 6-10ft. 

To open up the camera, I first removed the drip shield with a pair of pliers wrapped in painter's tape. Then, I pressed a roll of electrical tape against the retention ring and unscrewed it to reveal the internals of the camera:

![The inside of a G5 Bullet camera](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/camera-internals.jpg)

From there, it was only a matter of carefully turning the lens with the pliers to adjust the focus:

![Focusing the camera using a tape measure target](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/camera-focusing.jpg)

As it turns out, I ended up needing to further tweak the focus once the camera was installed, while at the very highest setting of my 20ft extension ladder:

![Focusing the camera with a test target](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/camera-focusing-nest.jpg)

This gave me a sharp image:

![The finished focused image](/img/posts/2025-02-20-my-ubiquiti-unifi-protect-bird-nest-camera-setup/camera-focused-nest.jpg)

That did the trick! I was sure to complete the work in late fall so as to not scare the finches away from the nesting site.