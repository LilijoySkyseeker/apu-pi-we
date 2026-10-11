# Computer vocabulary test 01: translation

Sources: `ui-strings.txt` (71 interface strings) and `email.txt`. Loans are adapted by hand with the Words-section sound rules (not run through `tools/names.py`). Brands and names keep their spelling after **en**. `[brackets]` mark a concept with no expression.

## UI

```
Settings
ge waka
Wi-Fi
wayifayi
Bluetooth
bulutufu
Notifications
ge iko la
Sound and vibration
ge nulu yen [vibration]
Display and brightness
du wuye yen wino
Battery
batali
Storage
pu kuwi
Privacy and security
mibun yen sonli
Password
apu pi udin
Account
[account]
Sign in
inwa
Sign out
kusa
Create an account
selo [account]
Forgot your password?
min yakin apu pi udin.
Search
walo geno
Save
kuwi
Save as
kuwi gan suso eni
Open
benbi
Close
tapi
Delete
yidu
Delete this file? This can't be undone.
min yidu fayilu tan. go mu lenu muge sigo bu.
Cancel
mu muge
OK
tayu
Copy
kopi
Paste
yaga
Cut
fonsu
Undo
muge sigo
Redo
muge moti
Share
neke
Download
dunu
Upload
sege tun bige
Install
insutolu
Update available
gun kubo duwa
Restart now
tuko moti eda
Turn off
muge bamo
File
fayilu
Folder
nansa
New folder
nansa duwa
Rename
kubo suso
Attach a file
manfu fayilu
Send
sege
Reply
febo
Reply all
febo tun we
Forward
sege tun eni
Inbox
ge dunu
Draft
ge mu sin sege
Sent
ge sege
Trash
ge yidu
Spam
supamu
Contacts
kontakutu la
Camera
kamela
Photos
foto la
Screenshot
foto pi du wuye
Loading...
le obu
No internet connection
gun intalunetu fa
Try again
walo moti
Something went wrong
batu in sin muwo
Page not found
mu geno mabo
Your changes have been saved
kubo la pi me gun kuwi
Are you sure you want to leave this page?
min me fule momu kusa mabo tan.
Allow access to your location?
min me efon wun to lugo kemu pi me.
Enable two-step verification
tuko miya gan lite sa
Low battery
batali nedin tapun
Charging
le muge kete
Airplane mode
lite pi du bina
Volume
dibon
Mute
muge mange
Keyboard
du tusi
Language
apu
Help
yema
```

## Email

```
From: Dana Morales
se en dana morales
Hi Kevin, I can't open the budget spreadsheet you shared with me this morning.
upe, en kevin. to mu lenu benbi mabo pi wifu pi nimo man me sin neke tun to nin leso tan.
When I click the link, it just says "You need permission" and asks me to request access.
wo to dandi [link], bu na oyi "me wupi efon" yen mido wun to mido efon li inwa.
I already sent a request, but nothing happened.
to sin sege mido, un musu fa sin muwo.
Could you check the sharing settings when you get a chance?
so nun miya ge waka pi neke, don me ibe muyi.

From: Kevin Park
se en kevin park
Sorry about that, Dana.
sepi gi ben, en dana.
I think I shared it with your personal Gmail address instead of your work account by mistake.
kon da to sin neke bu mu gan momu tun suso pi en gmail pi me, mu tun [account] pi doku.
I just added your work email as an editor, so it should open now.
ya foke fi, to sin yaga imeyilu pi doku pi me fu no kubo, gi tan kon te bu benbi eda.
If it still doesn't work, try signing out of Google and signing back in with your work login.
don bu le mu benbi, fon walo kusa en google yen inwa moti gan [account] pi doku.

From: Dana Morales
se en dana morales
Thanks, the file opens now, but it's really slow and keeps freezing when I scroll.
lota, fayilu benbi eda, un bu gun bi gake, yen bamo moti moti nin to kobi mabo.
My laptop fan is also running loud, so maybe the problem is on my end.
du gulo pi kamupuyutalu pi to wame le gun dibon, gi tan kon ka batu gun mon sanfi pi to.
Should I download a copy and open it in Excel instead?
min me momu wun to dunu kopi yen benbi bu gan fule en excel.

From: Kevin Park
se en kevin park
Please don't download it, because then we'll end up with two versions that don't match.
so nun mu dunu bu, gi pen win ibe kopi sa man mu kige.
Try closing your other browser tabs and clearing your cache first.
ya, fon walo tapi mabo eni la pi bulawusa pi me yen muge tapun kasu pi me.
If that doesn't help, restart your laptop and make sure your updates are installed.
don ben mu yema, fon tuko moti kamupuyutalu pi me, yen miya wun kubo duwa la gun insutolu.
The sheet has a lot of formulas, so it can be a bit heavy on older machines.
mabo pi wifu ibe folumula feli, gi tan kon da bu gun tason gogo li kamupuyutalu pani la.
Let me know if it's still freezing and I'll ask IT to take a look.
don bu le bamo, so iko to. de mido no yema kamupuyutalu li miya bu.
```

## Gaps

| Concept | How handled | How often a user meets it | Suggestion |
|---|---|---|---|
| computer (laptop, machine) | loan **kamupuyutalu** (6 syllables) | high | loan, clipped to a two-syllable root by the tools; built **du sunbu** "thing for counting" as an alternative |
| account (login identity) | [bracket] | high | root; nothing short builds it ("name that is registered" is a clause) |
| file | loan **fayilu** | high | loan **fayilu** |
| link | [bracket]; the loan **linku** is identical to **linku** "low" | high | root from the tools (loan is blocked) |
| copy | loan **kopi** | high | loan, but **kopi** drifts into **kobi** "move" (middle-consonant voicing); run it through the tools or give a root |
| search, seek | built **walo geno** "try to find" | high | root: "seek, look for" is a basic verb most languages have |
| delete, erase, remove | built **yidu** "take" | high | root "remove, erase"; **yidu** also had to carry Trash |
| share | built **neke** "give" | high | root "share, let others have too"; **neke** loses "you still have it" |
| settings | built **ge waka** "what is chosen" | high | root; **ge waka** reads as "a choice" |
| turn on / turn off, enable / disable | built **tuko** / **muge bamo** "start" / "make stop" | high | root pair on/off, pushed apart with `--antonym` |
| connect, connection | left out ("no internet" for "no internet connection") | high | root "connect, join"; **manfu** "tie" is the nearest |
| sound, noise | built **ge nulu** "what is heard" | high | root: a basic noun, odd to lack |
| screen, display | built **du wuye** "thing for showing" | high | compound **du wuye** in compounds.tsv; clip if it gets constant use |
| password | built **apu pi udin** "word of locking" | high | compound **apu pi udin**; clip later |
| undo | built **muge sigo** "make return" | high | compound **muge sigo** |
| update (noun and verb) | built **kubo duwa** "new change" / **muge duwa** "make new" | high | compound **kubo duwa** |
| page, sheet | **mabo** "paper" (the material) | high | sense note on **mabo** covering a page/sheet, or a root "page" |
| scroll | built **kobi mabo** "move the page" | high | compound **kobi mabo** |
| add (to a list, an editor) | built **yaga** "put" | high | root "add" |
| work, function (of a machine) | avoided ("still doesn't open") | high | extend **doku** "work" to machines, as Mandarin and German do; note it in the gloss |
| contact (address-book entry) | loan **kontakutu** | high | loan **kontakutu** |
| camera | loan **kamela** | high | loan **kamela** |
| Wi-Fi | loan **wayifayi** | high | loan **wayifayi** (or keep the brand spelling) |
| Bluetooth | loan **bulutufu** | medium | loan **bulutufu** (or keep the brand spelling) |
| keyboard | built **du tusi** "thing for writing" (could be a pen) | high | root "key, button", with keyboard built from it |
| privacy, private | built **mibun** "hide" | medium | root "private, not for others" |
| check, verify | built **miya** "look at" | medium | root "check, verify"; **miya** loses "confirm it's true" |
| vibrate, shake | [bracket] | medium | root "shake": basic verb |
| upload / download | built **sege tun bige** "send up" / **dunu** "get" | medium (download high) | keep **dunu**; compound **sege tun bige** |
| install | loan **insutolu** | medium | loan **insutolu** |
| trash, garbage | built **ge yidu** "what is removed" | medium | root "garbage": everyday household word |
| spam | loan **supamu** | medium | loan **supamu** |
| browser | loan **bulawusa** | medium | loan **bulawusa** |
| screenshot | built **foto pi du wuye** "photo of the screen" | medium | compound; shortens if screen gets a root |
| cache | loan **kasu** | low | loan **kasu** |
| formula | loan **folumula** (Latin form) | low | loan **folumula** |
