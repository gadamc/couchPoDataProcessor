function(doc) {
    if(doc.type == "daqdocument" && doc.status == "closed" && !doc.proc0){
	emit( doc.run_name, 1);
    }
}