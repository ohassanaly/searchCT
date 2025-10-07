fastAPI endpoint for the searchCT (search Clinical Trials) search engine

post requests @ search/

with query parameters :
"user_input" (the search engine query, natural text) ; example : "dose-finding in double-blind cryoglobulinemia vasculitis trial" ;<br>
"criteria" [optional] a list of sections among ['TITLE', 'JUSTIFICATION', 'OBJECTIVE', 'DESIGN', 'INCLUSION CRITERIA', 'EXCLUSION CRITERIA', 'INTERVENTION', 'STATISTICS'] to focus on for the search ;
