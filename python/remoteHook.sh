#!/usr/local/bin/tcsh

#set the version number of KDATA to use here explicitly
source $KDATA_ROOT/config/setup_kdata.csh #make sure environment variables are properly set

$KDATA_ROOT/lib/KDataPy/scripts/dataprocess/batchRunProc1.py https://edwdbuser:***@edwdbik.fzk.de:6984 datadb /sps/edelweis/kdata/dataprocessing/schedule
$KDATA_ROOT/lib/KDataPy/scripts/dataprocess/batchRunProc2.py https://edwdbuser:***@edwdbik.fzk.de:6984 datadb /sps/edelweis/kdata/dataprocessing/schedule