# Resources

## Goals for now

* Be able to fetch a single file or an archive of files

Resources and Resource Bundles

Resources will have:
  * name
  * path
  * option to add file hash
  * fetcher specific config

Resource Bundles will have:
  * contents:
    * list of:
      * path to file in archive (can use regex???)
      * filename/id to refer to it as
  * path to unpack
  * fetcher specific config 
    * archive type (zip, tar.gz)
