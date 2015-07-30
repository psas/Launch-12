## The Failure 

LV2.1 uses a standard dual-deploy parachute system: two commercial off-the-shelf (COTS) flight computers (a Telemetrum v3 and an ARTS) fire deploy a small drogue at apogee, the rocket falls quickly to a lower altitude, and then the main is deployed for a slow descent at touchdown.

In Launch-12, the main parachute deployed right at apogee, along with the drogue. It wasn't supposed to do this, and we were **extremely** lucky that the *20 minutes* (instead of like 2 minutes) it took to fall 5.1 km from apogee on the main chute, the rocket didn't drift many km away. This would have made recovery a total pain.

Here's a [video of the flight](https://www.youtube.com/watch?v=YUP2_m3gPiM) - you can see the main chutes come out at apogee (as well as the *camera fall out of the airframe and dangle on its Ethernet cord*... although that's another story.

## The Investigation

### Investigation 1: crossing main and apogee

We first blamed a failure of the wiring to the pyrotechnic charges. We have a total of 6 leads:

- 4 leads going to the LV2 Nose Separation Ring (NSR), any of which should fire the NSR and release the drogue.
- 2 leads going to two independent line cutters for releasing the main parachute.

We wired these e-matches to the COTS flight computers:

- Telemetrum
  - 2 NSR leads in parallel to "Apogee"
  - 1 line cutter to "Main"
- ARTS
  - 2 NSR leads in parallel to "Apogee" 
  - 1 line cutter to "Main"

If any of the "Main" and "Apogee" leads were crossed, then that would have explained the main deploying with the drogue. Post-flight, we ohm metered all of the leads and wires, and nothing was miswired. We blame Gavin's amazing color-coded, one-to-one connectorizing job that totally made this impossible. Yay Gavin!

### Investigation 2: Bad Main settings in the COTS FCs

Next we checked the logs from the Telemetrum and the ARTS FCs: perhaps one of the FCs had been misconfigured, and blew the chutes early?

The Telemetrum log said that it blew the apogee leads 2 seconds after apogee, and then blew the main at the correct altitude roughly 20 minutes later. So not the Telemetrum.

The ARTS log said it blew the apogee leads 2 seconds after apogee as well, and then the log timed out with no other events after XXX seconds. Because there were no other events many seconds after apogee, the ARTS wasn't to blame either.

### Investigation 3: Failure of the main chute retainer system

We thought that perhaps the loop / cord system that holds the main chute in at apogee somehow failed mechanically. Dave's investigation contradicted this: he found the line-cutter cut loop, and inspected that rope, and it all seemed correct.

That's when we found out that the main parachute bag was... missing.

### Investigation 4: failure of the main parachute bag.

We hypothesize that the main bag failed at apogee - it "zippered" off of its webbing that held the main chute down at apogee. This let the main chute, which is under tremendous pressure, "balloon" out into the air stream, where it caught the wind and deployed.

![Figure 1 - picture of whiteboard](photos/2015-07-22 00.17.57-resized.jpg "Figure 1: Main parachute failure mode")

In Figure 1 above, the drawing on the left shows how the main parachute is kept in place at apogee under normal circumstances. The middle drawing shows what we think happened in Launch-12: A very acute angle on the drogue pulled the webbing on the main bag off to one side, breaking some of the threads. This then zippered the bag, allows the parachute to come out of the recovery module and get into the airstream, as depicted in the drawing on the right.

So: does the physical evidence support this? In short, yes.

Figure 2 shows the angle of the drogue when it's first deployed. Note that the rocket has passed apogee, and is now accelerating down to the ground like a lawndart. The drogue parachute has deployed, and just inflated. The next few frames show the drogue "yanking" the rocket airframe violently around so that it's upright. In fact, in this process, the RasPi2 camera module is yanked out of its slide-out case and now dangles in the airstream by it's custom Ethernet cord.

![Figure 2 - Angle of Drogue Parachute](photos/screenshot-1.png "Figure 2: Angle of Drogue Parachute")

Figure 3 shows the blue main parachute bag poking out of the top of the recovery module a few seconds later. This shouldn't be happening at this point; the drogue line should be holding the bag down.

![Figure 3 - Main parachute bag poking out of the recovery module](photos/screenshot-2.png "Figure 3: Main parachute bag poking out of the recovery module")

Figure 4 shows the webbing from the blue main parachute flapping in the wind a few seconds after the main deploy. This shouldn't have happened; we should see the blue bag attached here :) 

![Figure 4 - Main parachute bag webbing flapping in the breeze](photos/screenshot-3.png "Figure 4: Main parachute bag webbing flapping in the breeze")

Figure 5 shows the webbing again - this time you can see the threads hanging out of the webbing.

![Figure 5 - Main parachute bag webbing with threads](photos/screenshot-4.png "Figure 5: Main parachute bag webbing with threads")

Figure 6 shows a shot of the nosecone with the small drogue bag still attached, which is what we expect.

![Figure 6 - Nosecone and drogue chute bag](photos/screenshot-5.png "Figure 6: Nosecone and drogue chute bag")

Figure 7 shows what we **think** is the zippered main parachute bag floating away at 5km, never to be found again, and showing that it somehow zippered off, thus letting the main out.

![Figure 7 - Goodbye main parachute bag](photos/screenshot-6.png "Figure 7: Goodbye main parachute bag")


