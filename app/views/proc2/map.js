function(doc) {
    if(doc && doc.type == "daqdocument" && doc.status == "good" && !doc.proc2 && doc.proc1 && doc.proc0){
	emit( doc.run_name, 1);
    }
}