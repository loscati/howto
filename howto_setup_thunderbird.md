# Thunderbird set-up

## Message font
The one used by Gmail, very readable and pretty is *Roboto*. Since all font used by Thunderbird are the one installed in the operating system, one only need to install the above-mentioned font to used in emails. 

The Font is freely downloadable from Google sites. For Manjaro/Arch Linux users this font is present in the official repositories under the name ``ttf-roboto``.

After that you need to selected as main font for messages.

+ **Preferences > Composition** under **HTML Style** select the *Roboto* font, with Medium size

## Signature for a single Email Account

1. Select the chosen Account
2. Select **Account Setting**, on the top right corner
3. On signature text select the **Use HTML** option
4. Append the signature

Since the font used for this is the *fixed font* one, I find a workaround to have *Roboto* also in the signature. Therefore, have consistency in the mail.
Because we selected option 3, we can use HTML to personalize the text.

In my case I did the following:
```html
<p style="font-family:roboto">
Leonardo Salicari<br>
Ph.D. Student in Complex Systems<br>
University of Padua<br>
Department of Physics and Astronomy "Galileo Galilei"<br>
</p>
```
I used the ``style`` attribute of ``p`` to select the *Roboto* font. In this way the signature is consistent with the mail body.

Lastly, to append the signature only on the first email, avoiding doing so on replies, do the following:
1. Select the chosen Account
2. Select **Account Setting**, on the top right corner
3. Go to **Composition and Addressing**
4. Deselect **Include signature for replies**