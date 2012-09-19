function(doc) {
    if(doc.type == "daqdocument" && doc.status == "bad"){
	emit( doc.run_name, 1);
    }
}