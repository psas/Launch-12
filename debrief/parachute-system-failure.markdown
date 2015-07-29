## Failure

LV2.1 uses a standard dual-deploy parachute system: two commercial off-the-shelf (COTS) flight computers (a Telemetrum v3 and an ARTS) fire deploy a small drogue at apogee, the rocket falls quickly to a lower altitude, and then the main is deployed for a slow descent at touchdown.

In Launch-12, the main parachute deployed right at apogee, along with the drogue. It wasn't supposed to do this, and we were **extremely** lucky that the *20 minutes* (instead of like 2 minutes) it took to fall 5.1 km from apogee on the main chute, the rocket didn't drift many km away. This would have made recovery a total pain.

## Investigation

### Investigation 1: crossing main and apogee

We first blamed a failure of the wiring to the pyrotechnic charges. We have a total of 6 leads:

- 4 leads going to the LV2 Nose Separation Ring (NSR), any of which should fire the NSR and relase the drogue.
- 2 leads going to two independent line cutters for releasing the main parachute.

We wired these e-matches to the COTS flight computers:

- Telemetrum
  - 2 NSR leads in parallel to "Apogee"
  - 1 line cutter to "Main"
- ARTS
  - 2 NSR leads in parallel to "Apogee" 
  - 1 line cutter to "Main"

If any of the "Main" and "Appogee" leads were crossed, then that would have explained the main deploying with the drogue. Post-flight, we ohm metered all of the leads and wires, and nothing was miswired. We blame Gavin's amazing color-coded, one-to-one connectorizing job that totally made this impossible. Yay Gavin!

### Investigation 2: Bad Main settings in the COTS FCs

Next we checked the logs from the Telemetrum and the ARTS FCs: perhaps one of the FCs had been misconfigured, and blew the chutes early?

The Telemetrum log said that it blew the apogee leads 2 seconds after apogee, and then blew the main at the correct altitude roughly 20 minutes later. So not the Telemetrum.

The ARTS log said it blew the apogee leads 2 seconds after apogee as well, and then the log timed out with no other events after XXX seconds. Because there were no other events many seconds after apogee, the ARTS wasn't to blame either.

### Investigtation 3: Failure of the main chute retainer system

We thought that perhaps the loop / cord system that holds the main chute in at apogee somehow failed mechanically. Dave's investigation contradicted this: he found the line-cutter cut loop, and inspected that rope, and it all seemed correct.

That's when we found out that the main parachute bag was... missing.

### Investigation 4: failure of the main parachute bag.

We hypothesize that the main bag failed at apogee - it "zippered" off of its webbing that held the main chute down at apogee. This let the main chute, which is under tremendous pressure, "balloon" out into the air stream, where it caught the wind and deployed.

![Figure 1 - picture of whiteboard](photos/2015-07-22 00.17.57-resized.jpg "Figure 1: Main parachute failure mode")




