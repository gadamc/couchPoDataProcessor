function(doc) {
    if(doc.type == "daqdocument" && doc.status == "closed" && !doc.proc0 && doc.Intitule != "Edelweiss 2, run 15"){
	emit( doc.run_name, 1);
    }
}