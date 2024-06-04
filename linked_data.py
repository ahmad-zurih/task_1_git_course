# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:38:40 2022

@author: as20q884 / André Scholl
"""
####################################################################################################################
###     Most Prolific Authors of Books
####################################################################################################################

from SPARQLWrapper import SPARQLWrapper, JSON               # Package to use SPARQL in Python.


def main():                                                 # Main part of the code
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")     # Access the SPARQL-Endpoint of DBpedia.
    sparql.setQuery("""
    PREFIX : <http://dbpedia.org/resource/>                  # Default namespace.
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>         # Of course possible to use XLM-Schemas in SPARQL.
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX dbonto: <http://dbpedia.org/ontology/>

	SELECT ?author (COUNT(DISTINCT ?uri) AS ?num_books)    # Choose author names and their number of uniquely identified books
	    WHERE {
	     { SELECT DISTINCT ?type ?typename WHERE {         # Part to select only the type and possible sub-classes of the category "Book".
               ?type rdfs:subClassOf* dbonto:Book ;         # We select a type that is a book (i.e., its URI) 
                                                            # or a sub-class of it, and the name of this type (i.e., more readable for humans).
		               rdfs:label ?typename .
		      FILTER (lang(?typename)='en')
		      }
	    }
	      ?uri  a ?type ;                              
		  rdfs:label ?title .                             # Title of each book.
	      FILTER (lang(?title)='en')
	    ?uri dbonto:author ?author_id .                   # Authors of books (i.e., their URIs) are stored in the variable ?author_id.
	  	?author_id rdfs:label ?author .                     # More human-readable complete name of authors in ?author
	    FILTER (LANG(?author)='en')
	}   GROUP BY ?author                                   # We group the number of books per each author (i.e., modality of the variable)
	    ORDER BY DESC(?num_books)                           # Sorting in descreasing number of books per each author
	    LIMIT 10                                           # Retrieve results only for the top ten most prolific authors
	""")
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    titles = results["head"]["vars"]  # Select the dictionary that has the value of keyword "head" in the first dictionary, 
    # and then the value of the keyword "vars" in this embedded dictionary
    
   # Basis JSON-result, from which the relevant values - i.e., of the keywords "author" and "num_hits" - are extracted with the for-loop under
    print(results["results"]["bindings"], "\n\n")
    
    with open("Most_prolific_authors.txt", "w") as file:        # Write in a .txt file
        for result in results["results"]["bindings"]:           # For-loop
            file.write(str(u"{:<24}\t{}".format(*[ result[f]["value"][:120] for f in titles ])) + "\n")  # Write formatted results in .txt file
            print(u"{:<24}\t{}".format(*[ result[f]["value"][:120] for f in titles ]))  # Print same formatted results in the console 
                                                                                        # on the right


       
if __name__ == "__main__":                                  # Run main part
    main()