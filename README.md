# Back end for dvd end point
version 0.0.1
## Overview 
This api endpoint is still in develop.

This endpoint should include api allow user to CRUD series, title, dvd, 
and genre tags.

In addition, a searching and paging function should also be implemented
so that font end can have  
## API design
### Entity definition:
1. Series:
A Franchise is a group of collection related title , movie. As such,
Series should be unique. A Series should include following fields:
-   uuid
-   name (Unique)
-   year (this is year of the first title released)
2. Title:
A title is a movie or a film series. Similar to franchise, each titile should
have unique name. A Titile should  should following fields:
-   uuid
-   name (Unique)
-   year (this is released year)
3.  DVD:
DVD is indicate number of resource at shop. As shop can have multiple copy of a 
titile, DVD objets's name is not required to be unique:
-   uuid
-   name 
4.  tags:
TBA

### Entity relationship:
1.  Series and Title:
Relation ship between series and title is one to many. A series can contain multiple titiles.

2. Titile and DVD:
Relation ship between series and title is one to many.

3.  Tags and other:
Relation ship between tags and other entities is many to many.

TBU

