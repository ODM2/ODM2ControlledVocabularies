# ODM2ControlledVocabularies
A Python/Django web application and REST API for managing the ODM2 Controlled Vocabularies.

This repository contains the source code for the master controlled vocabulary registry for the Observations Data Model 2 (ODM2).

The production Controlled Vocabulary website for ODM2 (which uses this code) can be accessed at:

http://vocabulary.odm2.org

### Accessing Vocabularies and Individual Terms

Each individual vocabulary can be accessed through the web user interface. For example:

http://vocabulary.odm2.org/actiontype/

Every term has a unique URL:

http://vocabulary.odm2.org/sitetype/stream/

Each vocabulary and term can also be accessed in Simple Knowledge Organization System (SKOS) format through a RESTful API.

* For a vocabulary: http://vocabulary.odm2.org/api/v1/actiontype/?format=skos
* For an individual term: http://vocabulary.odm2.org/api/v1/sitetype/stream/?format=skos

Vocabularies can also be exported in comma separated values (CSV) format.

### Modifying the Controlled Vocabularies

This web application provides moderated submission of new vocabulary terms and edits to existing terms. You can simply click on the "New" button on a vocabulary page or the "Edit" button on the page for an individual term to submit changes.

### Credits

This work was supported by National Science Foundation Grant [EAR-1224638](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1224638). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. 

