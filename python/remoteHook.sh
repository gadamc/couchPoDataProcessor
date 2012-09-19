#!/usr/local/bin/tcsh

#set the version number of KDATA to use here explicitly
set KDATA = $KDATA_ROOT
#set KDATA = /sps/edelweis/kdata/code/v4.5
source $KDATA/config/setup_kdata.csh #make sure environment variables are properly set

$KDATA/lib/KDataPy/scripts/dataprocess/batchRunProc1.py https://edwdbuser:***@edwdbik.fzk.de:6984 datadb /sps/edelweis/kdata/dataprocessing/schedule
#$KDATA/lib/KDataPy/scripts/dataprocess/batchRunProc2.py https://edwdbuser:***@edwdbik.fzk.de:6984 datadb /sps/edelweis/kdata/dataprocessing/schedule