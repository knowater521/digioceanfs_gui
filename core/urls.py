urls = (
    #'/','index.index',
    #'/','clustergroup.clustergroup',
	'/','clusternode.clusternode',
    '/clusterhome','index.index',
    '/indexgetnode','index.indexgetnode',
    '/indexgetdisk','index.indexgetdisk',
    '/indexgetraid','index.indexgetraid',
    '/indexgetupsinfo','index.indexgetupsinfo',
    '/indexgetreport','index.indexgetreport',
    '/indexgetfocus','index.indexgetfocus',
    '/indexgetreportmsg','index.indexgetreportymsg',
    '/indexgetservice','index.indexgetservice',
    '/clusterinitnavleft','index.initleftnav',
    '/login','index.login',
    '/logout','index.logout',
    '/changelanguage','index.changelanguage',
    '/password_modify','index.password_modify',
	'/password_check','index.password_check',
    #clusterguide
    '/clusterguide','clusterguide.clusterguide',
    '/clusterguide_group','clusterguide.clusterguidegroup',
    '/clusterguide_node','clusterguide.clusterguidenode',
    '/clusterguide_service','clusterguide.clusterguideservice',
    '/clusterguide_groupload','clusterguide.clusterguidegroupload',
    '/clusterguide_nodeload','clusterguide.clusterguidenodeload',
    '/clusterguide_serviceload','clusterguide.clusterguideserviceload',

    #clustergroup
    '/clustergroup','clustergroup.clustergroup',
    '/clustergroupload','clustergroup.clustergroupload',
    '/clustergroupcreate','clustergroup.clustergroupcreate',
    '/clustergroupadd','clustergroup.clustergroupadd',
    '/clustergroupedit','clustergroup.clustergroupedit',
    '/clustergroupdelete','clustergroup.clustergroupdelete',
    #cluternode
    '/clusternode','clusternode.clusternode',
    '/clusternodeload','clusternode.clusternodeload',
    '/clustergetnode','clusternode.clustergetnode',
    '/clusternodecreate','clusternode.clusternodecreate',
    '/clusternodereplace','clusternode.clusternodereplace',
    '/clusternodeview','clusternode.clusternodeview',
    '/clusternodeviewstaticinfo','clusternode.clusternodeviewstaticinfo',
    '/clusternodeviewstaticinfoxml','clusternode.clusternodeviewstaticinfoxml',
    '/clusternodeviewdynamicinfo','clusternode.clusternodeviewdynamicinfo',
    '/clusternodeviewdynamicinfoxml','clusternode.clusternodeviewdynamicinfoxml',
    '/clusternodedeletesingle','clusternode.clusternodedeletesingle',
    '/clusternodecifsrestart','clusternode.clusternodecifsrestart',
    '/clusternodenfsrestart','clusternode.clusternodenfsrestart',
    '/clusternodedisk','clusternode.clusternodedisk',
    '/clusternodenetwork','clusternode.clusternodenetwork',
    '/clusternodenetworkload','clusternode.clusternodenetworkload',
    '/clusternodesetipaddr','clusternode.clusternodesetipaddr',
    '/clusternodesetipaddr_single','clusternode.clusternodesetipaddr_single',
    '/clusternodesetbond','clusternode.clusternodesetbond',
    '/clusternodebonddel','clusternode.clusternodebonddel',
    '/clusternoderaidcreate','clusternode.clusternoderaidcreate',
    '/clusternoderaidload','clusternode.clusternoderaidload',
    '/clusternoderaidprogress','clusternode.clusternoderaidprogress',
    '/clusternoderaiddel','clusternode.clusternoderaiddel',
    '/clusternoderaidset_hs','clusternode.clusternoderaidset_hs',
    '/clusternoderaiddel_hs','clusternode.clusternoderaiddel_hs',
    '/clusternoderaiddel_select','clusternode.clusternoderaiddel_select',
    '/clusternodediskmap','clusternode.clusternodediskmap',
    '/clusternodedisk_update','clusternode.clusternodedisk_update',
    '/clusternoderaid_active','clusternode.clusternoderaid_active',
    '/clusternodedisk_active','clusternode.clusternodedisk_active',
	'/clusternodedisk_muti_op','clusternode.clusternodedisk_muti_op',
    '/clusternodereplacenodisk','clusternode.clusternodereplacenodisk',
    '/clusternodegetservicenodiskinfo','clusternode.clusternodegetservicenodiskinfo',
#    '/clusternodefileshare','clusternode.clusternodefileshare',
    #clusternodeview
    '/clusternodenetwork','clusternode.clusternodenetwork',
	'/clusternodesession','clusternode.clusternodesession',
    #clusterservice
    '/clusterservice','clusterservice.clusterservice',
    '/clusterserviceview','clusterservice.clusterserviceview',
    '/clusterserviceload','clusterservice.clusterserviceload',
    '/clusterserviceviewtabspage','clusterservice.clusterserviceviewtabspage',
    '/clusterserviceviewload','clusterservice.clusterserviceviewload',
    '/clusterserviceviewloadrefresh','clusterservice.clusterserviceviewloadrefresh',
    '/clusterservice_afr_syn','clusterservice.clusterservice_afr_syn',
    '/clusterservicecreateguide_a','clusterservice.clusterservicecreateguide_a',
    '/clusterservicecreateguide_b','clusterservice.clusterservicecreateguide_b',
    '/clusterservicecreateguide_c','clusterservice.clusterservicecreateguide_c',
    '/clusterservicecreatedisk','clusterservice.clusterservicecreatedisk',
    '/clusterservicecreateguide_c_afr_strip','clusterservice.clusterservicecreateguide_c_afr_strip',
    '/clusterservicecreateguide_c_strip_afr','clusterservice.clusterservicecreateguide_c_strip_afr',
    '/clusterservicecreate','clusterservice.clusterservicecreate',
    '/clusterservicecreatedialog','clusterservice.clusterservicecreatedialog',
    '/clusterservicextend','clusterservice.clusterservicextend',
    '/clusterservicextendservice','clusterservice.clusterservicextendservice',
    '/clusterservicextendnode','clusterservice.clusterservicextendnode',
    '/clusterservicecifsmanage','clusterservice.clusterservicecifsmanage',
    '/clusterservicecifsusermanage','clusterservice.clusterservicecifsusermanage',
    '/clusterservicecifslistuser','clusterservice.clusterservicecifslistuser',
    '/clusterservicecifsadduser','clusterservice.clusterservicecifsadduser',
    '/clusterservicecifsdeluser','clusterservice.clusterservicecifsdeluser',
    '/clusterservicecifschecklinks','clusterservice.clusterservicecifschecklinks',
    '/clusterservicecifschecklinksdata','clusterservice.clusterservicecifschecklinksdata',
    '/clusterservicecifsdellink','clusterservice.clusterservicecifsdellink',
    '/clusterservicecifs_status','clusterservice.clusterservicecifs_status',
    '/clusterservicecifsrestart','clusterservice.clusterservicecifsrestart',
    '/clusterservicenfs_status','clusterservice.clusterservicenfs_status',
    '/clusterservicenfsmanage','clusterservice.clusterservicenfsmanage',
    '/clusterservicenfsusermanage','clusterservice.clusterservicenfsusermanage',
    '/clusterservicenfslistuser','clusterservice.clusterservicenfslistuser',
    '/clusterservicenfschecklinks','clusterservice.clusterservicenfschecklinks',
    '/clusterservicenfschecklinksdata','clusterservice.clusterservicenfschecklinksdata',
    '/clusterservicenfsdellink','clusterservice.clusterservicenfsdellink',
    '/clusterservicenfsadduser','clusterservice.clusterservicenfsadduser',
    '/clusterservicenfsdeluser','clusterservice.clusterservicenfsdeluser',
    '/clusterservicenfsrestart','clusterservice.clusterservicenfsrestart',
	'/clusterservicesharemanage','clusterservice.clusterservicesharemanage',
    '/clusterservicexportstatus','clusterservice.clusterservicexportstatus',
    '/clusterservicestart','clusterservice.clusterservicestart',
    '/clusterservicestop','clusterservice.clusterservicestop',
    '/clusterservicerestart','clusterservice.clusterservicerestart',
    '/clusterservicedestroy','clusterservice.clusterservicedestroy',
#    '/clusterserviceedit','clusterservice.clusterserviceedit',
	'/clusterserviceraidlvdetail','clusterservice.clusterserviceraidlvdetail',
	'/clusterservicediskreplace','clusterservice.clusterservicediskreplace',
	'/clusterservicedisk','clusterservice.clusterservicedisk',
	'/clusterserviceraidload','clusterservice.clusterserviceraidload',
	'/clusterserviceraidload_select','clusterservice.clusterserviceraidload_select',
	'/clusterclientnodeload','clusterservice.clusterclientnodeload',
	'/clusterclientnodecreate','clusterservice.clusterclientnodecreate',
	'/clusterclientnodedelete','clusterservice.clusterclientnodedelete',
	'/clusterclientnodecifs','clusterservice.clusterclientnodecifs',
	'/clusterclientnodenfs','clusterservice.clusterclientnodenfs',
	'/clusterclientnodestatus','clusterservice.clusterclientnodestatus',
    #cluster notify
    '/clusternotify','clusternotify.clusternotify',
    '/clusternotifyload','clusternotify.clusternotifyload',
    '/clusternotifyinit','clusternotify.clusternotifyinit',
    '/clusternotifyfocus','clusternotify.clusternotifyfocus',
    '/clusternotifymsg','clusternotify.clusternotifymsg',
    '/clusternotifyfocusall','clusternotify.clusternotifyfocusall',
    '/clusternotifydelall','clusternotify.clusternotifydelall',
    #license page
    '/clusterlicense','clustertoolpage.clusterlicense',
    '/clustergetnodelist','clustertoolpage.clustergetnodelist',
    '/clustergetdeviceid','clustertoolpage.clustergetdeviceid',
    '/clusterchecklicense','clustertoolpage.clusterchecklicense',
    #get processing
    '/clustergetprocessing','clustertoolpage.clustergetprocessing',
    #manager check & set
    '/clustermanagercheck','index.manager_check',
    '/clustermanagerset','index.manager_set',
    '/clustergetmanagerip','index.manager_get',
    #session check
    '/checksession', 'clustertoolpage.clusterchecksession',
    #error
    #'/error', clustererror.error505,
)
