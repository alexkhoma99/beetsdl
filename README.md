# BeetsDL
A wrapper around `youtube-dl` for searching for songs and integrating them into your `beets` library (`beets` will handle renaming files and gathering metadata).
```
==> Searching for never gonna give you up ...
[1] Title: Rick Astley - Never Gonna Give You Up (Video)
    Channel: Official Rick Astley
    Duration: 3:33
    Views: 753,308,522 views

[2] Title: Rick Astley Never gonna give you up lyrics!!!
    Channel: Jaysean
    Duration: 3:46
    Views: 23,175,118 views

[3] Title: Rick Astley - Never Gonna Give You Up (The Roxy 1987)
    Channel: Official Rick Astley
    Duration: 2:58
    Views: 2,422,348 views

[4] Title: Never Gonna Give You Up Voice Crack
    Channel: MrMeme
    Duration: 1:56
    Views: 2,970,020 views

[5] Title: Rick Astley - Never Gonna Give You Up - Live at The Isle of Wight Festival 2019
    Channel: isleofwightfestival
    Duration: 5:06
    Views: 3,026,466 views

==> Enter choice (default 1): 1
[youtube] dQw4w9WgXcQ: Downloading webpage
[download] Destination: /tmp/tmpgkqv0g7v/Rick Astley - Never Gonna Give You Up (Video).webm
[download] 100% of 3.28MiB in 00:00
[ffmpeg] Destination: /tmp/tmpgkqv0g7v/Rick Astley - Never Gonna Give You Up (Video).mp3
Deleting original file /tmp/tmpgkqv0g7v/Rick Astley - Never Gonna Give You Up (Video).webm (pass -k to keep)

/tmp/tmpgkqv0g7v (1 items)
No matching release found for 1 tracks.
For help, see: http://beets.readthedocs.org/en/latest/faq.html#nomatch
[S]kip, Use as-is, as Tracks, Group albums, Enter search, enter Id, aBort? E
Artist: Rick Astley
Album: Never Gonna give you up
Finding tags for album "Rick Astley  - ".
Candidates:
1. Rick Astley - Never Gonna Give You Up (55.3%) (album, missing tracks, tracks) (7" Vinyl, 1987, GB, RCA, PB 41447)
2. Rick Astley - Never Gonna Give You Up (50.3%) (album, missing tracks, tracks) (12" Vinyl, 1987, XE, RCA, PT 41448)
3. Rick Astley - Never Gonna Give You Up (42.3%) (missing tracks, album, tracks) (12" Vinyl, 1987, CA, RCA, 6784-1-RD)
4. Rick Astley - Never Gonna Give You Up (39.4%) (missing tracks, album, tracks) (1987)
5. Rick Astley - The Best of Rick Astley: Never Gonna Give You Up (25.0%) (missing tracks, album, tracks) (CD, 2003, GB, BMG UK & Ireland, 82876 557482)
# selection (default 1), Skip, Use as-is, as Tracks, Group albums,
Enter search, enter Id, aBort?
Correcting tags from:
    Rick Astley  -
To:
    Rick Astley - Never Gonna Give You Up
URL:
    https://musicbrainz.org/release/dc919562-19c7-42c8-961c-7ed5520f00bb
(Similarity: 55.3%) (album, missing tracks, tracks) (7" Vinyl, 1987, GB, RCA, PB 41447)
 * Never Gonna Give You Up (Video) (#0) -> Never Gonna Give You Up (#1) (title)

```

### Usage
##### Requirements:
* youtube-dl
* beets

##### Install Instructions
* Download and setup `beets` ([see this guide](`https://beets.readthedocs.io/en/stable/guides/main.html`))
  * Enabling the `fromfilename` plugin can improve the importing step.
* Clone this repo
* Run `python3 setup.py install`

##### Usage
* Run `beetsdl "search term"`, where `"search term"` is what gets searched on YouTube (include the quotes).

### Future
This will be reworked into a proper `beets` plugin (invoked with `beet dl <search term>`), rather than a stand-alone tool.

