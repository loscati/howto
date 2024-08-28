# How to Zotero

Setup taken from this beautiful [post](https://ikashnitsky.github.io/2019/zotero/) by Kashnitsky.
The choice is based on Zotero being open-source and
in the ability to sync metadata in the Zotaro Cloud (300 Mb but enough) while
saving all PDFs in the Google Drive (15 Gb).

Two *plugins* are added:
1.  ZotFile: used to rename, following a rule chosen by the user, and organize
    PDFs in a separated folder
2.  Better BibTex: export the library into a plain .bib file

### Workflow to save a document (paper, book etc.)
> WARNING 2024/9: ZotFile [has no plan](https://github.com/jlegewie/zotfile/issues/655#issuecomment-1595364307) to support the recent Zotero 7 update.
> I'll probably need to rely on another plugin or stick with Zotero 6.x.x
1.  Drag the PDF into Zotero (in the collection chosen, e.g. Thesis)
2.  Rename it using **ZotFile** by right click on the item and selecting
    Manage Attachments --> Rename Attachments.
    NOTE: the success of the operation is marked by the file being saved
    in the local folder `/home/user/zotero-library`

This is the PDF which will be modified and synced into G Drive.
This operation leaves in Zotero only the synced file which will be
automatically synced into Drive, not the one manually dragged.


### Workflow to modify a paper
Modify (highlight, comment etc.) only the PDF saved in Zotero, i.e. the one
renamed and save in the zotaro-library folder (which is the one synced in Drive).
Same if you want to modified remotely, you need tio modify the file in the corresponding Drive folder and then sync everything.


### Where are my files?
Drive: `gdrive/zotero-library` (classified by Author, see
Zotaro settings)

Local: `/home/user/zotero-library`

### How are metadata synced?
Through the automatic sync system of Zotero.
This does not require any action from the user, it is automatic when Zotero is opened.


### How are PDFs synced?
This is done manually by the user by connecting the zotero-library directory
to Drive.
I use `rclone` on Manjaro, command line software to synchronize with all
major cloud services.
Basically a bash script allow me to upload data. This operation is done by the
following command:
```bash
rclone sync ~/zotero-library gdrive:/zotero-library --fast-list -P
```
where `--fast-line` is used to speed up the operation (this is something related
to Drive) and `-P` displays a static information chart in the terminal to
keep track of the progress.


### How to create a `.bib` file
Go into the collection (e.g thesis) and use:
`export collection -> Better BibTex`
checking the *Keep update* box.


### Export library in other machines
In a fresh new machine, just follow the same instructions of the original post
of Kashnitsky and Zotero will take care of sync all metadata and PDFs from
clouds.
