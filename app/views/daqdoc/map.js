function(doc) {
    if(doc.type == "daqdocument"){
	emit( doc.run_name, 1);
    }
}