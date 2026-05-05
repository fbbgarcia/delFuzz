# Default Costs

A reference for the default character and token-level edit costs used by delFuzz. All substitution costs are bidirectional — only one direction is listed here for brevity.

## Character-Level Costs

### Substitution Costs

| Char(s) 1 | Char(s) 2 | Cost |
| --- | --- | --- |
| a | á | 0.10 |
| a | ä | 0.25 |
| e | é | 0.10 |
| i | í | 0.10 |
| i | y | 0.50 |
| o | ó | 0.10 |
| o | ö | 0.25 |
| u | ú | 0.10 |
| u | ü | 0.25 |
| u | v | 0.50 |
| n | ñ | 0.25 |
| y | ÿ | 0.25 |
| b | v | 0.50 |
| c | s | 0.50 |
| c | z | 0.50 |
| c | q | 0.50 |
| s | z | 0.50 |
| g | j | 0.50 |
| ph | f | 0.50 |

### Insertion Costs

| Char(s) | Cost |
| --- | --- |
| h | 0.50 |

### Deletion Costs

| Char(s) | Cost |
| --- | --- |
| h | 0.50 |

## Token-Level Costs

### Substitution Costs

| Token(s) 1 | Token(s) 2 | Cost |
| --- | --- | --- |
| Beto | Alberto | 0.15 |
| Beto | Roberto | 0.15 |
| Beto | Albert | 0.25 |
| Beto | Robert | 0.25 |
| Alberto | Albert | 0.15 |
| Roberto | Robert | 0.15 |
| Pancho | Francisco | 0.15 |
| Pancho | Francis | 0.25 |
| Paco | Francisco | 0.15 |
| Paco | Francis | 0.25 |
| Francisco | Francis | 0.15 |
| Chofo | Rodolfo | 0.15 |
| Chofo | Rudolph | 0.25 |
| Rodolfo | Rudolph | 0.15 |
| Chepe | José | 0.15 |
| Chepe | Joseph | 0.25 |
| Pepe | José | 0.15 |
| Pepe | Joseph | 0.25 |
| José | Joseph | 0.15 |
| Meme | Manuel | 0.15 |
| Manuel | Manola | 0.15 |
| Manuel | Manolo | 0.15 |
| Alejo | Alejandro | 0.15 |
| Alejo | Alexander | 0.25 |
| Fonsi | Alfonso | 0.15 |
| Fonsi | Alphonse | 0.25 |
| Poncho | Alfonso | 0.15 |
| Poncho | Alphonse | 0.25 |
| Jano | Alejandro | 0.15 |
| Jano | Alexander | 0.25 |
| Alejandro | Alexander | 0.15 |
| Chejo | Sergio | 0.15 |
| Chus | Jesús | 0.15 |
| Chuy | Jesús | 0.15 |
| Adi | Adolfo | 0.15 |
| Adi | Adolph | 0.25 |
| Adolfo | Adolph | 0.15 |
| Güicho | Luis | 0.15 |
| Güicho | Louis | 0.25 |
| Lucho | Luis | 0.15 |
| Lucho | Louis | 0.25 |
| Luis | Louis | 0.15 |
| Luis | Louise | 0.15 |
| Chente | Vicente | 0.15 |
| Chente | Vincent | 0.25 |
| Vicente | Vincent | 0.15 |
| Kiko | Federico | 0.15 |
| Kiko | Frederick | 0.25 |
| Federico | Frederick | 0.15 |
| Lalo | Eduardo | 0.15 |
| Lalo | Edward | 0.25 |
| Eduardo | Edward | 0.15 |
| Lencho | Lorenzo | 0.15 |
| Lencho | Lawrence | 0.25 |
| Lorenzo | Lawrence | 0.15 |
| Memo | Guillermo | 0.15 |
| Memo | William | 0.25 |
| Guillermo | William | 0.15 |
| Mingo | Domingo | 0.15 |
| Mingo | Dominic | 0.25 |
| Domingo | Dominic | 0.15 |
| Neto | Ernesto | 0.15 |
| Neto | Earnest | 0.25 |
| Ernesto | Earnest | 0.15 |
| Nando | Fernando | 0.15 |
| Nando | Ferdinand | 0.25 |
| Fernando | Ferdinand | 0.15 |
| Monchi | Ramón | 0.15 |
| Monchi | Raymond | 0.25 |
| Ramón | Raymond | 0.15 |
| Rulo | Raúl | 0.15 |
| Nacho | Ignacio | 0.15 |
| Nacho | Ignatius | 0.25 |
| Nancho | Ignacio | 0.15 |
| Nancho | Ignatius | 0.25 |
| Ignacio | Ignatius | 0.15 |
| Toño | Antonio | 0.15 |
| Toño | Anthony | 0.25 |
| Antonio | Anthony | 0.15 |
| Quique | Enrique | 0.15 |
| Quique | Henry | 0.25 |
| Enrique | Henry | 0.15 |
| Goyo | Gregorio | 0.15 |
| Goyo | Gregory | 0.25 |
| Gregorio | Gregory | 0.15 |
| Miguel | Michael | 0.15 |
| Juan | John | 0.15 |
| Pablo | Paul | 0.15 |
| Adán | Adam | 0.15 |
| Agustín | Augustine | 0.15 |
| Alfonso | Alfonse | 0.15 |
| Alfonso | Alonso | 0.15 |
| Alfonse | Alonso | 0.15 |
| Alfredo | Alfred | 0.15 |
| Ambrosio | Ambrose | 0.15 |
| Andrés | Andrew | 0.15 |
| Armando | Herman | 0.15 |
| Arturo | Arthur | 0.15 |
| Bartolomé | Bartholomew | 0.15 |
| Bautista | Baptiste | 0.15 |
| Benito | Benedict | 0.15 |
| Bernardino | Bernardo | 0.15 |
| Bruno | Brown | 0.15 |
| Buenaventura | Bonaventura | 0.15 |
| Carlos | Charles | 0.15 |
| Cornelio | Cornelius | 0.15 |
| Cristián | Christian | 0.15 |
| Cristóbal | Christopher | 0.15 |
| Darío | Darius | 0.15 |
| Desi | Desiderio | 0.15 |
| Diego | Santiago | 0.15 |
| Edgardo | Edgar | 0.15 |
| Edmundo | Edmund | 0.15 |
| Emilio | Emile | 0.15 |
| Esteban | Stephen | 0.15 |
| Eusebio | Eusebius | 0.15 |
| Fabio | Fabius | 0.15 |
| Fabricio | Fabrice | 0.15 |
| Felipe | Philip | 0.15 |
| Félix | Felix | 0.15 |
| Fermin | Firmin | 0.15 |
| Geraldo | Gerald | 0.15 |
| Gerardo | Gerard | 0.15 |
| Gustavo | Gustav | 0.15 |
| Herberto | Herbert | 0.15 |
| Hernán | Hernando | 0.15 |
| Hugo | Hugh | 0.15 |
| Jacobo | Jacob | 0.15 |
| Jaime | James | 0.15 |
| Javier | Xavier | 0.15 |
| Jerónimo | Jerome | 0.15 |
| Joaquín | Joachim | 0.15 |
| Joaquín | Joachin | 0.15 |
| Jorge | George | 0.15 |
| Josue | Joshua | 0.15 |
| Julio | Julius | 0.15 |
| Leonardo | Leonard | 0.15 |
| Leopoldo | Leopold | 0.15 |
| Luciano | Lucian | 0.15 |
| Marcelo | Marcellus | 0.15 |
| Marcio | Marcus | 0.15 |
| Marco | Mark | 0.15 |
| Mateo | Matthew | 0.15 |
| Matías | Matthias | 0.15 |
| Maximiliano | Maximilian | 0.15 |
| Máximo | Maximus | 0.15 |
| Agusto | Agustus | 0.15 |
| Heracio | Hoartio | 0.15 |
| Heracio | Horatius | 0.15 |
| Cruz | Cross | 0.15 |
| Cruz | Cruzita | 0.15 |
| Chema | José María | 0.15 |
| Chema | Joseph Mary | 0.15 |
| Juampa | Juan Pablo | 0.15 |
| Juampa | John Paul | 0.15 |
| Juandi | Juan Diego | 0.15 |
| Juandi | John Diego | 0.15 |
| Juanjo | Juan José | 0.15 |
| Juanjo | John Joseph | 0.15 |
| Juanfran | Juan Francisco | 0.15 |
| Juanfran | John Francis | 0.15 |
| Juancho | Juan Francisco | 0.15 |
| Juancho | John Francis | 0.15 |
| Juanfer | Juan Fernando | 0.15 |
| Juanfer | John Ferdinand | 0.15 |
| Luismi | Luis Miguel | 0.15 |
| Luismi | Louis Michael | 0.15 |
| Licha | Alicia | 0.15 |
| Licha | Alice | 0.25 |
| Alicia | Alice | 0.15 |
| Calu | Claudia | 0.15 |
| Chayo | Rosario | 0.15 |
| Chayo | Rosary | 0.25 |
| Rosario | Rosary | 0.15 |
| Concha | Concepción | 0.15 |
| Concha | Conception | 0.25 |
| Concha | Conchita | 0.15 |
| Conchita | Chita | 0.15 |
| Concepción | Conception | 0.15 |
| Lena | Magdalena | 0.15 |
| Lena | Magdalene | 0.25 |
| Magdalena | Magdalene | 0.15 |
| Leti | Leticia | 0.15 |
| Leti | Letitia | 0.25 |
| Leticia | Letitia | 0.15 |
| Luchi | Lucía | 0.15 |
| Luchi | Lucy | 0.25 |
| Lucía | Lucy | 0.15 |
| Mar | Mariana | 0.15 |
| Mar | Marianna | 0.15 |
| Mar | Maryanne | 0.25 |
| Mariana | Marianna | 0.15 |
| Mariana | Maryanne | 0.15 |
| Tita | Marta | 0.15 |
| Tita | Martha | 0.25 |
| Marta | Martha | 0.15 |
| Meches | Mercedes | 0.15 |
| Pili | Pilar | 0.15 |
| Paquita | Francisca | 0.15 |
| Paquita | Frances | 0.25 |
| Francisca | Frances | 0.15 |
| Pepita | Josefa | 0.15 |
| Pepita | Josephine | 0.25 |
| Josefa | Josephine | 0.15 |
| Tina | Cristina | 0.15 |
| Tina | Christine | 0.25 |
| Tina | Christina | 0.25 |
| Cristina | Christine | 0.15 |
| Cristina | Christina | 0.15 |
| Vicky | Victoria | 0.15 |
| Vivi | Viviana | 0.15 |
| Vivi | Vivianne | 0.25 |
| Viviana | Vivianne | 0.15 |
| Geli | Angélica | 0.15 |
| Gela | Angélica | 0.15 |
| Lola | Dolores | 0.15 |
| Fani | Estefanía | 0.15 |
| Fani | Stephanie | 0.25 |
| Estefanía | Stephanie | 0.15 |
| Lupe | Guadalupe | 0.15 |
| Chavela | Isabela | 0.15 |
| Chavela | Isabelle | 0.25 |
| Isabela | Isabelle | 0.15 |
| Isabela | Isabel | 0.15 |
| Isabelle | Isabel | 0.15 |
| Chío | Rocío | 0.15 |
| Sandy | Sandra | 0.15 |
| Clementina | Cleme | 0.15 |
| María | Mary | 0.15 |
| Adelita | Adele | 0.15 |
| Alejandra | Alexandra | 0.15 |
| Ana | Anna | 0.15 |
| Anabella | Annabel | 0.15 |
| Antonietta | Antonia | 0.15 |
| Anunciación | Annunziata | 0.15 |
| Ascención | Ascension | 0.15 |
| Asunción | Asumption | 0.15 |
| Beatriz | Beatrix | 0.15 |
| Blanca | Blanche | 0.15 |
| Camila | Camilla | 0.15 |
| Caridad | Charity | 0.15 |
| Carla | Carlota | 0.15 |
| Carmela | Carmel | 0.15 |
| Carmelita | Carmel | 0.15 |
| Carmen | Carmel | 0.15 |
| Carmina | Carmel | 0.15 |
| Catalina | Katherine | 0.15 |
| Catherina | Catherine | 0.15 |
| Clarisa | Clarissa | 0.15 |
| Constanza | Constance | 0.15 |
| Consuelo | Consolation | 0.15 |
| Débora | Deborah | 0.15 |
| Delfina | Delphina | 0.15 |
| Dominga | Dominique | 0.15 |
| Elena | Helen | 0.15 |
| Elena | Ileana | 0.15 |
| Eloisa | Eloise | 0.15 |
| Ema | Emma | 0.15 |
| Emilia | Emily | 0.15 |
| Emilia | Amelia | 0.15 |
| Emperatriz | Empress | 0.15 |
| Ernesta | Ernest | 0.15 |
| Esmeralda | Emerald | 0.15 |
| Esperanza | Hope | 0.15 |
| Estela | Estelle | 0.15 |
| Estela | Star | 0.15 |
| Eugenia | Eugenie | 0.15 |
| Evangelina | Evangeline | 0.15 |
| Evita | Eva | 0.15 |
| Faustina | Faustus | 0.15 |
| Feliciana | Feliciano | 0.15 |
| Filomena | Philomena | 0.15 |
| Florentina | Florence | 0.15 |
| Florinda | Flora | 0.15 |
| Gabriela | Gabrielle | 0.15 |
| Gabriela | Gabriella | 0.15 |
| Genoveva | Genevieve | 0.15 |
| Gracia | Grace | 0.15 |
| Hortensia | Hortense | 0.15 |
| Inés | Agnes | 0.15 |
| Inmaculada | Immaculate | 0.15 |
| Isidora | Isidore | 0.15 |
| Ivette | Yvette | 0.15 |
| Jacinta | Hyacinth | 0.15 |
| Leonor | Eleanor | 0.15 |
| Lidia | Lydia | 0.15 |
| Liliana | Lillian | 0.15 |
| Lorena | Lorraine | 0.15 |
| Lorenza | Lauren | 0.15 |
| Lucila | Lucille | 0.15 |
| Margarita | Margaret | 0.15 |
| Marita | María | 0.15 |
| Matilde | Matilda | 0.15 |
| Mayra | Myra | 0.15 |
| Bethlehem | Belén | 0.15 |
| Alba | Dawn | 0.15 |
| Dawn | Aurora | 0.15 |
| Gloria | Geoffrey | 0.15 |
| Dorothy | Donato | 0.15 |
| Majo | María José | 0.15 |
| Majo | Mary Joseph | 0.15 |
| Anabel | Ana Belen | 0.15 |
| Anabel | Ana Bethlehem | 0.15 |
| Anaisa | Ana Isabel | 0.15 |
| Anaisa | Ana Isabelle | 0.15 |
| Maribel | María Isabel | 0.15 |
| Maribel | Mary Isabelle | 0.15 |
| Mabel | María Isabel | 0.15 |
| Mabel | Mary Isabelle | 0.15 |
| Mafer | María Fernanda | 0.15 |
| Mafer | Mary Fernanda | 0.15 |
| Mayte | María Teresa | 0.15 |
| Mayte | Mary Teresa | 0.15 |
| Malena | María Elena | 0.15 |
| Malena | Mary Elena | 0.15 |
| Marianela | María Estela | 0.15 |
| Marciela | María Celia | 0.15 |
| Maricarmen | María del Carmen | 0.15 |

### Insertion Costs

| Token(s) | Cost |
| --- | --- |
| de | 0.20 |
| del | 0.20 |
| la | 0.10 |
| los | 0.10 |
| las | 0.10 |
| Juan | 0.15 |
| José | 0.15 |
| María | 0.15 |

### Deletion Costs

| Token(s) | Cost |
| --- | --- |
| de | 0.20 |
| del | 0.20 |
| la | 0.10 |
| los | 0.10 |
| las | 0.10 |