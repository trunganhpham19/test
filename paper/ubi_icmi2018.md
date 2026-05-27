Introducing WESAD, a Multimodal Dataset for Wearable
Stress and Affect Detection
PhilipSchmidt∗ AttilaReiss,RobertDürichen, KristofVanLaerhoven
RobertBoschGmbH ClausMarberger UniversityofSiegen
CorporateResearch,Germany RobertBoschGmbH Siegen,Germany
firstname.lastname@de.bosch.com CorporateResearch,Germany kvl@eti.uni-siegen.de
ABSTRACT 1 INTRODUCTION
Affectrecognitionaimstodetectaperson’saffectivestatebased Affectivecomputingisanemergingfield,inspiredbythevision
on observables, with the goal to e.g. improve human-computer toimprovehuman-computerinteractionbybuildingempathicma-
interaction. Long-term stress is known to have severe implica- chines.Empathicmachinesdetecttheaffectivestateofahuman
tionsonwellbeing,whichcallforcontinuousandautomatedstress user,adapttheir’behaviour’accordingly,andmightevenexhibit
monitoringsystems.However,theaffectivecomputingcommu- ownemotionaltraits.Fromahealthcarepointofview,stress,de-
nitylackscommonlyusedstandarddatasetsforwearablestress finedas’nonspecificresponseofthebodytoanydemanduponit’
detectionwhicha)providemultimodalhigh-qualitydata,andb) [25],isaparticularlyinterestingaffectivestate.Thisisduetothe
includemultipleaffectivestates.Therefore,weintroduceWESAD, harmfuleffectsoflong-termstress,whichcanrangefromheadaches
anewpubliclyavailabledatasetforwearablestressandaffectde- andtroubledsleepingtoanincreasedriskofcardiovasculardiseases
tection.Thismultimodaldatasetfeaturesphysiologicalandmotion [4,16,22].AccordingtotheBritishHealthandSafetyExecutive
data,recordedfrombothawrist-andachest-worndevice,of15 (HSE),stressaccountedfor37%ofallwork-relatedillhealthcases
subjectsduringalabstudy.Thefollowingsensormodalitiesare in2015/16[1].Theseseveresideeffectsofstresscallforautomated
included:bloodvolumepulse,electrocardiogram,electrodermal detectionmethods.
activity,electromyogram,respiration,bodytemperature,andthree- Inordertobuildareliablestressdetectionsystem,itisimportant
axisacceleration.Moreover,thedatasetbridgesthegapbetween tounderstandthatstressisprimarilyaphysiologicalresponsetoa
previouslabstudiesonstressandemotions,bycontainingthree stimulus,triggeredbythesympatheticnervoussystem(SNS).Dur-
differentaffectivestates(neutral,stress,amusement).Inaddition, ingthisresponseamixtureofhormoneslikecortisoloradrenaline
self-reportsofthesubjects,whichwereobtainedusingseverales- arereleased,leadingtoanincreasedbreathing/heartrateandmus-
tablishedquestionnaires,arecontainedinthedataset.Furthermore, cletension.Thesephysiologicalchangespreparetheorganismfora
abenchmarkiscreatedonthedataset,usingwell-knownfeatures physicalreaction(’fight-or-flight’).AsshownbyKreibigetal.[13]
andstandardmachinelearningmethods.Consideringthethree- thephysiologicalresponsestocertainemotionalstimuliarealsoto
classclassificationproblem(baselinevs.stressvs.amusement),we someextentspecific.Apsychologicalmodelwellsuitedforcaptur-
achievedclassificationaccuraciesofupto80%.Inthebinarycase ingaffectivestatesisRussel’scircumplexmodel[23].Accordingto
(stressvs.non-stress),accuraciesofupto93%werereached.Finally, thismodel,affectivestatescanbemappedintoa2Dspace,using
weprovideadetailedanalysisandcomparisonofthetwodevice forexampletheaxesvalenceandarousal.Thevalencedimension
locations(chestvs.wrist)aswellasthedifferentsensormodalities. indicateshownegative/positiveanaffectivestateisperceived.On
thearousalaxis,whichisknowntobeimpactedbystress[9],the
KEYWORDS stateisratedintermsofexcitement.
Affectivecomputing,Emotionrecognition,Stressdetection,Multi- Inrecentyears,thespecificityofthephysiologicalresponsesto
modaldataset,Sensorfusion,Benchmark,Userstudy stressandemotionalstimuliwasutilisedtotrainmachinelearn-
ingmodelstopredicttheaffectivestateofasubject.Usingdeep
ACMReferenceFormat:
neuralnetworks,trainedonaudioand/orvisualdata,ahighperfor-
PhilipSchmidt,AttilaReiss,RobertDürichen,ClausMarberger,andKristof
manceinemotionclassificationisachieved[17,29].However,these
VanLaerhoven.2018.IntroducingWESAD,aMultimodalDatasetforWear-
modelsarequitedemandingintermsofcomputationalresources
ableStressandAffectDetection.In2018InternationalConferenceonMulti-
modalInteraction(ICMI’18),October16–20,2018,Boulder,CO,USA.ACM, andareonlypartiallyapplicableonembeddeddevices.Classify-
NewYork,NY,USA,9pages.https://doi.org/10.1145/3242969.3242985 ingstressfromaudiosampleswasalsosuccessfullydone,e.g.,by
Lu[14].However,recordingaudioand/orvideodatacontinuously
∗AlsowithUniversityofSiegen.
isintermsofprivacyquiteintrusive,andconcerningtechnical
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor feasibilitydifficult.Hence,thesemodalitiesareonlyavailablein
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed specificoccasions.Wearableelectronicdevices,incontrast,areonly
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
minimallyintrusive.Deviceslikesmartphones/watchesarealready
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, popularamongusers.Contemporarywearablescanbeusedtotrack
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora stepsandmonitorotherphysicalactivities.Tokeepupwiththe
fee.Requestpermissionsfrompermissions@acm.org.
currenttrendtoquantifyvitalfunctions,adesirablenextstepis
ICMI’18,October16–20,2018,Boulder,CO,USA
©2018AssociationforComputingMachinery. toinferaffectivestatesbasedonmultimodalwearablesensordata.
ACMISBN978-1-4503-5692-3/18/10...$15.00 Plarreetal.[20]andHovsepianetal.[8]trainedstressdetection
https://doi.org/10.1145/3242969.3242985

systemsonperipheralphysiologicaldatautilisingelectrocardio- distinguishingeightdifferentmoodswithasubject-independentac-
gram(ECG),respiration(RESP)and3-axisaccelerometer(ACC) curacyof62.14%.However,asthesystemwastrainedandtestedon
data,recordedbyachest-worndevice.Gjoreskietal.[5]usedthe onlyfoursubjects,thegeneralisationpropertiesarequestionable.
dataofawrist-worndevicerecordingbloodvolumepulse(BVP), Although there is intensive research in the field of affective
electrodermalactivity(EDA),skintemperature(TEMP),andACC computingfromwearabledevices,thereisonlyverylittlepublicly
totrainastressdetectionmodel.Inordertodetectemotionsin availabledata.Healeyetal.[6]publishedadatasetondriverstress.
responsetomusic,Kimetal.[10]usedECG,RESP,EDA,andelec- ThisdatasetfeaturesECG(496Hz),EDA(31Hz),RESP(31Hz),
tromyogram(EMG)data.Distinguishingstressandemotionsisnot andEMG(15.5Hz)data.Moreover,Picardetal.[19]publisheda
atrivialtask,sincebothhaveastrongimpactontheautonomous datasetcontainingphysiologicaldatarecordedfromoneperson,
nervoussystem.However,incurrentaffectivecomputingresearch, whoissubjecttoeightdifferentemotionalstimuliover20days.
stressandemotiondetectionfromwearablesarecommonlytackled Morerecently,Koestraetal.[12]publishedDEAP,adatabasefor
astwodisjointtopics.Ourworkaddressesthisshortcoming.Thisis emotionanalysisusingphysiologicalsignals.Thedatasetcontains
importantsince,foraholisticaffectiveusermodel,assessingboth electroencephalogram(EEG)(512Hz),facialvideosandperipheral
stressandemotionsisrequired. physiologicalsignals(recordedat512Hz,thendown-sampledto
Asoutlinedabove,multimodalsetupshavebeenusedforstress 256Hz).Thedatawasrecordedwhilethesubjectswatched40one-
oremotiondetectiontasks.However,incontrasttomanyother minuteexcerptsfrommusicvideos.Thefinal40clipswerechosen
research fields, there is a lack of commonly used, standardised fromalargerpoolofvideos,byaskingvolunteerstoratetheclips
benchmarkingdatasetsforstressandaffectdetection.Hence,itis intermsoftheirvalenceandarousalvalueandthenchoosingthe
difficulttocompareresultsobtainedbydifferentresearchers.Our onesthathadthestrongestratingwiththesmallestvariance.
workintendstoaddressthisshortcomingaswell. Thewayhumansperceiveandreacttoanaffectivestimulusis
Themaincontributionsofthispaperarethreefold: verysubjectdependent.Hence,personalisationisanimportant
(1) Anewmultimodal,publiclyavailabledataset1ispresented. issue.Inordertotrainpersonalisedmodels,subjectiveratingsof
The data has been recorded using two different devices thedifferentaffectivestimuliarerequired.Theseratingsarecom-
(onechest-basedandonewrist-based),eachincludinghigh- monlygeneratedbyself-assessmentofthesubjects.Forinstance,
resolutionphysiological(BVP,ECG,EDA,EMG,RESP,and manikinscanbeusedtogeneratepersonalisedvalence,arousal,
TEMP)andmotion(ACC)modalities. dominance,andlikinglabels[12].InthestudyofPlarreetal.[20]
(2) Thedatasetbridgesthegapbetweenpreviouslabstudieson subjectsreportedtheirstresslevelsbyansweringfivequestions
stressandemotions,bycontainingthreedifferentaffective (Cheerful?,Happy?,Angry/Frustrated?,Nervous/Stressed?,Sad?)
states(neutral,stress,amusement).Inaddition,thedataset onafourpointscale(NO,no,yes,YES).Otherstudiesemployed
featuresself-reportedvaluesontheperceivedaffectivestate morecomplexquestionnairessuchasthePANAS[18]andSTAI
ofthesubjects,whichwereobtainedusingseveralestab- [5]. In field studies, smart phone apps offer ideal platforms for
lishedquestionnaires.Theseself-reportscanbeusedtotrain self-reports,e.g.,onmood[32].
personalisedclassifiers. Inthispaperwepresentanoveldatasetforstressandaffect
(3) Abenchmarkiscreatedusingalargeamountofwell-known
detection.Thesubjects(n=15)wereexposedtodifferentaffective
features(extractedfromphysiologicalandmotionsignals) stimuli(stressandamusement).Inaddition,abaselineandtwo
andcommonmachinelearningmethods(DecisionTree(DT), meditationperiods(introducedtode-excitetheparticipantsaftera
RandomForest(RF),AdaBoost(AB),LinearDiscriminant stimulus)wererecorded.Thedatasetcontainshighresolutionphys-
Analysis(LDA)andk-nearestneighbour(kNN)). iological(ECG,EDA,EMG,RESP,andTEMP)andmotion(ACC)
datasampledat700Hzfromachest-worndevice,andlowerresolu-
2 RELATEDWORK tiondatafromawrist-worndevice.Finally,thedataofeachsubject
islinkedtoseveralself-reports,whichrepresentthesubjectiveex-
Inrecentyears,anumberofstudieshavebeenconductedwiththe
perienceduringanaffectivestimulus.Thedatasetiswell-suitedto
aimtoelicitanddetectstressbasedonphysiologicalparameters.
benchmark(personalised)stressandaffectdetectionalgorithms,a
Forthispurpose,stressorslikepublicspeaking,mentalarithmeticor
firstevaluationispresentedinthispaper.
physicalstressors(e.g.coldpressor)wereemployed[5,8,20].How-
ever,theseapproachesfocusondetectingandclassifyingstressful
vs.non-stressfulstatesanddonottakeanyotheraffectivestates 3 DATACOLLECTION
intoaccount.ClassicalmachinelearningalgorithmsliketheRF
Thissectionprovidesdetailsonthesubjects,employedsensors,
wereemployedtothestressclassificationtask,achievinga72%ac-
sensor placement, the study protocol, and the self-reports. The
curacyonathreeclass(no,low,highstress)problem[5].Kimetal.
studywasapprovedbytheworkerscouncilandthedatasecurity
[10]usedfoursongstoelicitdifferenttargetemotions,whichwere
officerofourresearchcenter.
thenclassifiedusingLDA,achievingasubject-independentcorrect
classificationratioof70%.However,thetopicofcombiningstress
andemotiondetectionsystemshasonlyreceivedlittleattention. 3.1 Participants
Zenonosetal.[32]presentedamoodrecognitionsystemcapableof Duetothedefinedstudyprotocol,wespecificallytargetedgraduate
studentsatourresearchfacility.Exclusioncriteria,statedinthe
1Thedatasetintroducedinthispaperismadepubliclyavailable,andcanbedownloaded
studyinvitation,werepregnancy,heavysmoking,mentaldisorders,
from:https://ubicomp.eti.uni-siegen.de/home/datasets/icmi18/.

RespiBAN andE4 weresynchronisedmanuallyviaadoubletap
gesture.
Baselinecondition:Afterthesubjectshadbeenequippedwith
thesensors,a20minutebaselinewasrecorded.Duringthebaseline
thesubjectsweresitting/standingatatableandneutralreading
material(magazines)wasprovided.Thebaselineconditionaimed
atinducinganeutralaffectivestate.
Amusementcondition:Duringtheamusementcondition,the
subjectswatchedasetofelevenfunnyvideoclips.Eachclipwas
followedbyashortneutralsequenceoffiveseconds.Eightofthe
shortclipswerechosenfromthecorpuspresentedbySamsonetal.
[24].Theremainingthreevideoswerechosenbytheauthors.In
Figure 1: Placement of the RespiBAN and the ECG, EDA, total,theamusementconditionhadalengthof392seconds.
EMG,TEMPsensors. Stresscondition:Thesubjectswereexposedtothewell-studied
Trier Social Stress Test (TSST) [11], which consists of a public
speakingandamentalarithmetictask.Thesetasksareknownto
chronicandcardiovasculardiseases.Intotal,17subjectspartic-
elicitstressreliably[20],astheyaresocialevaluativeandinflict
ipatedinourstudy.Duetosensormalfunction,thedataoftwo
a high mental load on the subjects. In our version of the TSST,
participantshadtobediscarded.Theremaining15subjectshada
thestudyparticipantsfirsthadtodeliverafiveminutespeechon
meanageof27.5 ± 2.4years.Twelvesubjectsweremaleandthe
theirpersonaltraitsinfrontofathree-personpanel,focusingon
otherthreesubjectswerefemale.
strengthsandweaknesses.Thesubjectsweretoldthatthethree
3.2 SensorSetupandPlacement panelmemberswerehumanresourcesspecialistsfromourresearch
facility.Inordertoboosttheircareeroptions,thesubjectsweretold
Forthedatacollection,weusedbothachest-andawrist-worn
totrytoleavethebestpossibleimpression.Thestudyparticipants
device:aRespiBANProfessional2andanEmpaticaE43,respectively.
hadthreeminutestopreparetheirspeechbuttheywerenotallowed
The RespiBAN itself is equipped with sensors to measure ACC
tousetheirnotesduringthepresentation.Afterthespeech,the
and RESP, and can function as a hub for up to four additional
panelaskedthesubjectstocountfrom2023tozero,doingsteps
modalities.Usingthefouranalogports,ECG,EDA,EMG,andTEMP
of17.Moreover,wheneverthesubjectsmadeamistake,theyhad
wererecorded.Allsignalsweresampledat700Hz.TheRespiBan
tostartover.Forbothtasks,thesubjectsweregivenfiveminutes
wasplacedaroundthesubject’schest(seeFigure1).TheRESPis
bythepanelandhencetheTSSThadatotallengthofaboutten
recordedviaarespirationinductiveplethysmographsensor.The
minutes.AftertheTSSTthestudyparticipantsweregivenaten-
ECGdatawasrecordedviaastandardthreepointECG.Inorderto
minuterestperiod.
allowthesubjecttomoveasfreelyaspossible,theEDAsignalwas
Meditation:Theamusementandstressconditions,whichboth
recordedontherectusabdominis(theabdomenhasahighdensity
aimedatexcitingthesubjects,werefollowedbyaguidedmeditation.
ofsweatglands[28],hencesuitableforEDAmeasurement)and
Theaimofthismeditationwasto’de-excite’thesubjectsandbring
theTEMPsensorwasplacedonthesternum.TheEMGdatawas
thembacktoaclosetoneutralaffectivestate.Themeditationwas
recordedontheuppertrapeziusmuscleonbothsidesofthespine.
basedonacontrolledbreathingexercise,instructedviaanaudio
Inordertoavoidwirelesspacketloss,therecordeddatawasstored
track.Subjectsfollowedtheinstructionswithclosedeyes,while
locallyandtransferredtoacomputerforfurtherprocessingafter
sittinginacomfortableposition.Themeditationhadadurationof
theexperiment.AllsubjectsworetheEmpaticaE4ontheirnon-
sevenminutes.
dominanthand.TheE4recordsBVP(64Hz),EDA(4Hz),TEMP(4
Recovery:Attheendoftheprotocol,thesensorswereagain
Hz),andACC(32Hz).
synchronised via a double tap gesture. Then, the sensors were
removedandthesubjectswereinformedthatthepanelmembers
3.3 StudyProtocol
werejust’normal’researchers.
Thegoalofthestudywastoelicitthreedifferentaffectivestates Intotal,thestudyhadadurationofabouttwohours.Figure2
(neutral,stress,amusement)intheparticipants.Inaddition,the summarisestheprotocol(withoutthepreparationandtherecovery
subjectswereaskedtofollowaguidedmeditationinordertode- period). As detailed above, our lab protocol features two major
excitethemafterthestressandamusementconditions.Thedifferent stimuli:anamusementconditionandastressfulcondition.These
partsofthestudyprotocolaredetailedbelow: twoconditionswereinterchanged(seeFigure2)betweendifferent
Preparation:Theparticipantshadtoavoidcaffeineandtobacco subjectsinordertoavoideffectsoforder.Inadditiontothesestim-
inthehourbeforetheexperimentwastobegin.Further,thesubjects uli,abaselineandtwomeditationperiodswererecorded.Inorder
wereaskedtodonostrenuousexerciseonthedayofthestudy. toinducevarianceinthesubjects’posture,thebaseline,amusement
Priortothestudytheparticipantsreadandsignedaconsentform. andstressconditionswereconductedeitherstandingorsitting.For
Uponarrivalatthestudylocation,theparticipantswereequipped eachcondition,approximatelyhalfofthesubjectswerestanding
withthesensorsandashortsensortestwasconducted.Thenthe andtheotherhalfweresitting.Duringthemeditation,however,all
2http://www.biosignalsplux.com/en/respiban-professional subjectswereseated.
3http://www.empatica.com/research/e4/

VersionA contextrecognition(e.g.Reissetal.[21]).Allfeatures(exceptfor
statistical-andfrequency-domainEMG-features,seebelow)based
Baseline Amusement MediI Stress Rest MediII onphysiologicalsignalswerecomputedwithawindowsizeof60
seconds.ThiswindowsizewaschosenfollowingKreibigetal.[13].
InTable1,thefeaturesextractedfromthedifferentmodalitiesare
VersionB displayed.
OntherawACCsignaldifferentstatisticalfeatures,e.g.themean
Baseline Stress Rest MediI Amusement MediII µacc,iandstandarddeviationσacc,iwerecomputed.Thesefeatures
werecomputedbothforeachaxisseparately(i ∈{x,y,z})andas
absolutemagnitudes,summedoverallaxes(3D).Inaddition,the
Figure2:Thetwodifferentversionsofstudyprotocol.The peakfrequencywascomputedforeachaxisseparatelyf peak .
acc,i
red/darkboxesrefertofillinginself-reports. OntherawECG/BVPsignaltheheartbeatswerefoundbasedon
peakdetectionalgorithms.Usingthepeaks,theheartrate(HR)and
correspondingstatisticalfeatures(mean,standarddeviation)were
3.4 ObtainingGroundTruth
computed.Moreover,fromthelocationoftheheartbeatstheheart
Inordertovalidatethestudyprotocol,wecollectedfiveself-reports ratevariablility(HRV)wasderived,whichisanimportantstarting
of each participant (timing indicated by red/dark boxes in Fig- pointforadditionalfeatures.Forinstance,theenergyindifferent
ure2).Eachoftheself-reportscontainedseveralquestionnaires. frequencybands(fx )wascomputed.Thefrequencybands(x)
HRV
Firstly,participantsfilledinaPositiveandNegativeAffectSchedule used,weretheultralow(ULF:0.01-0.04Hz),low(LF:0.04-0.15Hz),
(PANAS),whichconsistsof20items(tenpositiveandtennegative high(HF:0.15-0.4Hz)andultrahigh(UHF:0.4-1.0Hz)band.In[15]
items)eachratedonafivepointLikertscale.PANASreliablyas- theHRandHRVaredescribedindetail.
sessespositive(PA)andnegativeaffect(NA),whicharetwolargely TheEDAiscontrolledbythesympatheticnervoussystem(SNS),
independentdimensions[30].PAreachesfrom’sadandlethargic’ andhenceitisparticularlysensitivetohigharousalstates.First,a
(lowvalue)to’concentratedandenergetic’(highvalue).NAranges 5HzlowpassfilterwasappliedtotherawEDAsignal,similarto
from’calmness’(lowvalue)to’subjectivedistress’(highvalue). relatedwork[26,27].Then,statisticalfeatureswerecomputed(e.g.
Furthermore,weaddedtheitemsStressed?,Frustrated?,Happy?,and mean,standarddeviation,dynamicrange,etc.).Furthermore,the
Sad?,whichwerescoredbythesubjectsusingthesamescaleas rawEDAsignalconsistsofatonic(referredtoasskinconductance
inPANAS.Theseitemscanbeusedtogeneratethesamelabels level(SCL))andaphasic(skinconductanceresponse(SCR))com-
asusedbyPlarreetal.[20].Secondly,similartoGjoreskietal.[5], ponent.TheSCLrepresentsaslowlyvaryingbaselineconductivity,
weusedsixitemsfromtheState-TraitAnxietyInventory(STAI) whiletheSCRisashorttermresponsetoastimulus.Inorderto
togaininsightintotheanxietyleveloftheparticipants.Theitems separatethesetwocomponents,themethodproposedbyChoiet
werechosenaccordingtotheirfactorloads[2],andscoredona al.[3]wasapplied.AfterseparatingtheSCLandSCR,additional
fourpointLikertscale.Thirdly,weusedSelf-AssessmentManikins features,e.g.numberofpeaksintheSCR(#SCR),werecomputed.
(SAM)togeneratelabelsinthevalence-arousalspace[12].Finally, DetailsabouttheEDA-relatedfeaturescanbefoundinChoietal.
aftertheTSST,nineitemsfromtheShortStressStateQuestionnaire [3]andHealeyetal.[6].
(SSSQ)[7]wereaddedtothequestionnairesinordertoidentify TwodifferentprocessingchainswereappliedtotherawEMG
whichtypeofstress(worry,engagement,ordistress)wasmost signal.Inthefirstchain,theDCcomponentwasremovedbyap-
prevalentinthesubjects.Thevaluesfromthesequestionnairescan plyingahighpassfilter.Then,thefilteredsignalwascutinto5-
beseenassubjectivereportsonhowtheparticipantsfeltduringa secondwindows,andstatisticalandfrequency-domainfeatures
conditionandmaybeusedtotrainpersonalisedmodels.However, (e.g.peakfrequency)werecomputed.Inaddition,thespectralen-
forthefirstevaluationpresentedinthispaper,weusedthestudy ergy(PSD(fEMG))wascomputedinsevenevenlyspacedfrequency
protocolasgroundtruth. bandsfrom0to350Hz.Followingthesecondprocessingchain,a
lowpassfilter(50Hz)wasappliedtotherawEMGsignal.Next,the
4 METHODS processedsignalwassegmentedinto60-secondwindows.Onthese
peaks
Theanalysisandevaluationofourdatasetfollowstheclassical windows different peak features, e.g. number # EMG and mean
dataprocessingchain,consistingofthefollowingsteps:prepro- amplitudeµ Amp ,werecomputed.Foramoredetaileddescription
EMG
cessing,segmentation,featureextraction,andclassification.Details ofEMG-basedfeatures,wereferthereadertoWijsmanetal.[31].
onthesedifferentstepsarepresentedbelow(thefirstthreesteps BeforecomputingfeaturesontheRESPsignal,abandpassfilter
areexplainedtogethersincetheydependonthespecificsensor (cutofffrequencies:0.1and0.35Hz)wasapplied.Next,apeakdetec-
modality). torwasusedtoidentifyminimaandmaxima.FollowingPlarreetal.
[20]themeanandstandarddeviationoftheinhalation/exhalation
4.1 FeatureExtraction (µI ,σI , µE ,andσE)werecomputed.Inaddition,theratiobetween
Segmentationofthe(preprocessed)sensorsignalswasdoneusing inhalationandexhalation(I/E),stretchranдeRESP,inspirationvol-
aslidingwindow,withawindowshiftof0.25seconds.TheACC- umevolinsp,respirationraterateRESP,andrespirationduration
(cid:80)
featureswerecomputedwithawindowsizeoffiveseconds,as werederived RESP [20].
similarwindowlengthsarebroadlyappliedforacceleration-based

Table1:Listofextractedfeatures.Abbreviations:#=number 4.2 ClassificationAlgorithms
(cid:80)
of, =sumof,STD=standarddeviation.
Theextractedfeatures,detailedabove,serveasinputfortheclassi-
ficationstep.Fivemachinelearningalgorithmswereappliedand
Feature Description comparedwithinourbenchmark:DecisionTree(DT),RandomFor-
| µACC,i,σACC,i |     | Mean,STDforeachaxissepa- |     |
| ------------- | --- | ------------------------ | --- |
i∈{x,y,z,3D} ratelyandsummedoverallaxes est(RF),AdaBoost(AB),LinearDiscriminantAnalysis(LDA),and
(cid:82)
ACC ∥ ACC,i ∥ i∈{x,y,z,3D} Absoluteintegralforeach/allaxes k-NearestNeighbour(kNN).Astheentiredataprocessingchain
f p ea k j∈{x,y,z} Peakfrequencyforeachaxisi wasimplementedinPython,weusedthescikit-learnimplementa-
A C C ,j
µHR,σHR Mean,STDoftheHR tionoftheaforementionedclassifiers.FortheABensemblelearner,
µHRV,σHRV Mean,STDoftheHRV decisiontreewasusedasbaseestimator.Foreachofthedecision-
| NN50,pNN50 |     | #andpercentageofHRVinter- |     |
| ---------- | --- | ------------------------- | --- |
tree-basedclassificationalgorithms(DT,RF,AB),informationgain
valsdifferingmorethan50ms
wasusedtomeasurethequalityofsplittingdecisionnodes,and
| TINN |     | Triangularinterpolationindex |     |
| ---- | --- | ---------------------------- | --- |
theminimumnumberofsamplesrequiredtosplitanodewasset
| rmsHRV |     | RootmeansquareoftheHRV |     |
| ------ | --- | ---------------------- | --- |
fx to20.Thenumberofbaseestimatorswassetto100forbothofthe
| ECG HRV |     | Energyinultralow,low,high, |     |
| ------- | --- | -------------------------- | --- |
and x∈{ULF,LF,HF,UHF} andultrahighfrequency ensemblelearners(RFandAB).Moreover,aLDAandakNN(with
| BVP |     | componentoftheHRV |     |
| --- | --- | ----------------- | --- |
fLF/HF k=9)classifierwereusedforclassification.
RatioofLFandHFcomponent
HRV
| (cid:80)f |     | (cid:80) thefreq.components |     |
| --------- | --- | --------------------------- | --- |
x
| x∈{ULF,LF,HF,UHF} |     | inULF-HF |     |
| ----------------- | --- | -------- | --- |
4.3 EvaluationMetric
| relx f |     | Relativepoweroffreq. |     |
| ------ | --- | -------------------- | --- |
component WeusedaccuracyandF1-scoreasevaluationmetrics.Accuracy
LFnorm,HFnorm NormalisedLFandHF representsthenumberofcorrectlyclassifiedinstancesoutofall
component
µEDA,σEDA samples.TheF1-scoreisdefinedastheharmonicmeanofpreci-
Mean,STDoftheEDAsignal
minEDA,maxEDA sion,indicatingthereliabilityoftheresultsinacertainclass,and
Minandmaxvalue
∂EDA,ranдeEDA
Slopeanddynamicrange recall,representingameasureofcompleteness.Toobtainthefinal
µSCL,σSCL,σSCR
Mean,STDoftheSCR/SCL F1-score,precisionandrecallwerecomputedforeachclasssepa-
corr(SCL,t)
EDA CorrelationbtwSCLandtime ratelyandthenaveraged.ApplyingtheF1-scoreisrecommended
#SCR
#identifiedSCRsegments forunbalancedclassificationtasks,whichisthecasewhenusing
| (cid:80)A m | p,(cid:80)t | (cid:80) |     |
| ----------- | ----------- | -------- | --- |
SCRstartlemagnitudesand WESAD(sincethevariousconditionswerecarriedoutatdiffer-
SC R SCR
responsedurations
(cid:82) entlengthsduringthestudyprotocol).Allmodelswereevaluated
| scr |     | AreaundertheidentifiedSCRs |     |
| --- | --- | -------------------------- | --- |
usingtheleave-one-subject-out(LOSO)cross-validation(CV)pro-
| µEMG,σEMG |     | Mean,STDofEMGsignal |     |
| --------- | --- | ------------------- | --- |
cedure.Hence,theresultsindicatehowamodelwouldgeneralise
| ranдeEMG |     | Dynamicrange |     |
| -------- | --- | ------------ | --- |
(cid:82) andperformondataofapreviouslyunseensubject.
| ∥             | ∥   | Absoluteintegral     |     |
| ------------- | --- | -------------------- | --- |
| EMG EMG       |     |                      |     |
| π(cid:72) EMG |     | MedianoftheEMGsignal |     |
5 RESULTSANDDISCUSSION
| P10 | ,P90 | 10thand90thpercentile |     |
| --- | ---- | --------------------- | --- |
EMG EMG
f ,f (cid:72) EMG, Thissectionprovidesfirstananalysisofthecollectedself-reports.
| µ E MG |     | Mean,medianand |     |
| ------ | --- | -------------- | --- |
fpeak Second,detailedresultsontheevaluationoftherecordedsensor
Peakfrequency
EMG
PSD(fEMG) Energyinsevenbands data and processing chain are given, including a discussion on
#peaks theimportanceofthedifferentsensormodalitiesandextracted
| EMG |     | #peaks |     |
| --- | --- | ------ | --- |
µAmp,σAmp features.Forthedataanalysisandevaluationpresentedhere,we
Mean,STDofpeakamplitudes
E M G E M G onlyconsiderthedatarecordedduringthebaseline,stress(TSST),
| (cid:80) A m | p,(cid:80)¯ A m p | (cid:80) (cid:80) |     |
| ------------ | ----------------- | ----------------- | --- |
EMG EMG andnormalised of andamusementpartsofthestudyprotocol(seeFigure2.)
peakamplitudes
| µx,σx |     | Mean,STDofinhalation(I) |     |
| ----- | --- | ----------------------- | --- |
RESP x∈{I,E} 5.1 EvaluationoftheSelf-reports
andexhalation(E)duration
| I/E |     | Inhalation/exhalationratio |     |
| --- | --- | -------------------------- | --- |
ranдeRESP,volinsp Stretch,Volume Inthiswork,theanalysisoftheself-reportedmeasures(seesubsec-
rateRESP Breathrate tion3.4)hasbeenusedtoverifythatthedesignoftheexperimental
(cid:80) Respirationduration conditionswassuitabletomanipulatethesubjects’affectivestate
RESP
µTEMP,σTEMP Mean,STDoftheTEMP asdesired.Table2showstheresults(meanandstandarddeviation)
TEMP
minTEMP,maxTEMP Min,maxTEMP ofthethreemeasuresandsubscales,respectively.
ranдeTEMP Dynamicrange Comparingtheself-reportsaftertheamusementandbaseline
| ∂TEMP |     | Slope |     |
| ----- | --- | ----- | --- |
conditionrevealsthattheamusementconditionhadthedesired
effect:thesubjectsreportslightlyhigherscoresonvalenceand
arousal(dimensionalapproach,DIM)andlessanxiety(STAI).How-
ever,theeffectoftheconditionisrathersmall.Incontrast,the
impactofthestressconditionispronounced,acrossallquestion-
| On the raw TEMP | signal common | statistical features | (mean, |
| --------------- | ------------- | -------------------- | ------ |
naires.TheanalysisoftheSSSQscoresindicatesthatthesubjects
standarddeviation,min,max,etc.)werecomputed.Inaddition,the
feltmoreengagedandworriedthandistressedduringtheTSST
| slopeofthesignal∂ | isusedasafeature. |     |     |
| ----------------- | ----------------- | --- | --- |
TEMP task(Engagement:11.7±2.3,Distress:6.0±2.9,Worry:10.6±2.3).

Table2:Evaluationofthequestionnaires. Thedataconsideredinthispaper(belongingtothethreeaffec-
tivestatesofinterest)amounttoapproximately36minutesper
PANAS DIM subject.With15subjectsandusingaslidingwindowof0.25sec-
STAI
positive negative valence arousal onds,approximately133000windowsweregenerated.Outofthese
Baseline 25.5±6.0 12.3±2.0 10.8±1.9 6.7±0.9 2.5±0.9 windows,53%belongtothebaselineclass,30%representthestress
Stress 31.3±4.7 22.0±6.4 18.5±2.0 4.5±1.6 6.8±1.8
class,and17%originatefromtheamusementcondition.Inthelast
Amusement 25.8±5.1 11.4±2.1 9.3±2.0 7.5±0.6 3.0±1.6
tworowsofTable3thebaselineF1-score/accuracyofarandomand
asophisticatedguesseronthethree-classproblemaredisplayed.
Therandomguesserisdefinedtochooseoneofthethreepossible
Thehigh’Engagement’scoremightresultfromthesubjects’high classesatrandom,thusreachinganaccuracyof33%andaF1-score
motivationtoperformwellinthegiventask.Thehigh’Worry’ of32%.Incontrast,thesophisticatedguesserwouldalwayschoose
scoresuggeststhatthesubjectsweredeterminedtogiveagood themajorityclass.Hence,asophisticatedguesserwouldreachan
impressiononthepanel.Inouropinion,thesescoresdemonstrate accuracyof53%.However,its’F1-scorewouldonlybe32%.Inthe
thatmostsubjectsbelievedourcoverstoryoftheTSST. twolastrowsofTable4,thesametypeofrandomandsophisticated
Afterthestresscondition,thePANASshowedincreasedscores guesserarepresentedforthebinaryclassificationtask.
withrespecttopositive(PA)andnegativeaffect(NA).Thehigh Comparingtheperformanceoftheemployedalgorithms,onthe
PAscoreindicatesthatsubjectsfeltenergisedandconcentrated three-classtask(Table3)andbinaryclassificationtask(Table4),it
duringtheTSST,whichcoincideswiththehighengagementvalues becomesapparentthattheensemble-basedmethods(RF,AB)and
reportedintheSSSQ.TheelevatedNAscoreindicatesanincreased theLDAreachedsimilarclassificationscores.Dependingonthe
levelofsubjectivedistress.TheDIMscoressupporttheseobserva- inputmodalities,theseclassifiersreachscoresupto80%forthe
tions,indicatinganincreaseinarousalandadecreaseinvalence. three-classproblemandupto93%forthebinarytask,respectively.
Moreover,theSTAIshowselevatedvaluesaftertheTSST,asex- ConcludingfromTable3andTable4,thekNNhadtheoverallworst
pectedforsubjectsinastressfulcondition.Thestatisticaldifference performance,reachingaccuraciesofatmost60%onthethree-class
betweenthebaselineandstressconditionswereconfirmedwiththe problem,and78%inthebinarytask.
Wilcoxonsigned-ranktest.Overall,theexperimentalprotocol(es- Using only motion-based features (wrist and/or chest ACC)
peciallywithrespecttothestresscondition)isconsideredsuitable leadstoconsiderablylowerclassificationscorescomparedtore-
toinducethedesiredaffectivestates. sultsobtainedusingphysiologicalfeatures.Thissuggeststhatthe
physiology-basedfeaturesprovideadeeperinsightintotheaffec-
5.2 EvaluationofSensorModalitiesand
tivestatesofthesubjectsthanthemotionpatterns.Moreover,we
ExtractedFeatures canruleoutthepossibilitythatourclassifiersonlylearnedtodis-
tinguishbetweenmotionpatternscharacteristicfortheconditions
Basedontheaffectivestatesofthestudyprotocol(baseline,stress,
oftheprotocol.
andamusementcondition),wedistinguishtwoclassificationtasks.
Inthethree-classproblemtheaccuraciesusingoneofthewrist-
First,athree-classproblemwasdefined:baselinevs.stressvs.amuse-
basedphysiologicalmodalitiesrangefrom59%to70%.Usingone
ment.ResultsonthisclassificationtaskarepresentedinTable3.
ofthephysiologicalchest-basedmodalitiesonthesameclassifi-
Second,abinaryclassificationtaskwasdefinedbycombiningthe
cationproblem,accuraciesbetween54%and72%arereached.In
statesbaselineandamusementtoanon-stressclass,posingthestress
thebinaryclassificationtasktheaccuraciesusingawrist-based
vs.non-stressclassificationproblem.Resultsofthisclassification
inputmodalityrangefrom69%to86%andtheaccuraciesusing
taskarepresentedinTable4.Forbothclassificationtasks,16differ-
oneofthechest-basedmodalitiesrangefrom67%to88%.Inboth
entmodalitycombinationsareevaluated:
classificationtaskstheRESPisaparticularlystrongchest-based
• eachofthefourmodalitiesofthewrist-baseddevicesepa-
modalityleadingtothebestresultofasinglemodality.Besides
rately(ACC,BVP,EDA,andTEMP)
thestress-relatedchangesintherespiration,thiscanbepartially
• eachofthesixmodalitiesofthechest-baseddeviceseparately
explainedconsideringthefactthatthestudyparticipantsspokedur-
(ACC,ECG,EDA,EMG,RESP,andTEMP)
ingtheTSST.Hence,theclassifiersmighthavepartiallylearnedto
• allmodalitiesofonedevice(wristorchest)
distinguishbetweenspeaking(stresscondition)andnon-speaking
• allphysiologicalmodalitiesofonedevice(sameaslastentry,
episodes(baselineandamusementcondition).Inbothclassification
butwithoutACC)
tasks,usingonlytheTEMPdata,eitherchestorwrist-based,as
• allmodalitiesfrombothdevices(wristandchest)together
inputleadstolowclassificationscores.Obviously,TEMPisnota
• allphysiologicalmodalitiesfrombothdevicestogether(same
well-suitedmodalitytosolelybasetheclassificationofaffective
aslastentry,butwithoutACC)
statesupon.Comparingtheresultsobtainedusingonlythewrist-or
Finally,theevaluationwasperformedusingeachofthefivema- chest-basedEDAdata,thelatterseemstoholdmorerelevantinfor-
chinelearningalgorithms,specifiedpreviously.Eachsetup(defined mationleadingtosomewhathigheraccuraciesinbothclassification
bytheclassificationtask,appliedclassifier,andincludedsensor tasks.Incontrast,comparingtheperformanceofclassifierssolely
modalities)wasrunfivetimes,toreportmeanandstandarddevia- relyingontheBVPorECGdata,theformerleadstoslightlyhigher
tionoftheevaluationmetrics(F1-scoreandaccuracy).SinceLDA accuracies.Theresultsreachedusingallphysiologicalchest-based
andkNNaredeterministicclassifiers,onlythemeanvaluesare modalities(three-classaccuracy:80%,binaryaccuracy:93%)are
reported. higherthantheonesobtainedusingallphysiologicalwrist-based

Table3:Evaluationofthegivenmodalitiesandclassifiersonthethree-class(baselinevs.stressvs.amusement)classification
task.Abbreviations:DT=DecisionTree,RF=RandomForest,AB=AdaBoostDT,LDA=Lineardiscriminantanalysis,kNN=
k-nearestneighbour
|     |     | DT  |     | RF  |     | AB  |     | LDA | kNN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F1-score Accuracy F1-score Accuracy F1-score Accuracy F1-score Accuracy F1-score Accuracy
Motion:
ACCwrist 43.91±1.16 53.71±0.91 46.50±0.26 56.40±0.16 46.38±0.64 57.20±0.57 36.27 47.73 37.20 45.54
ACCchest 42.18±0.4 51.14±0.29 41.96±0.29 53.48±0.29 44.28±0.75 56.56±0.70 34.61 48.84 31.07 40.29
Wrist:
BVP 51.15±0.31 57.57±0.22 53.83±0.11 64.09±0.12 53.29±0.16 64.46±0.21 54.72 70.17 50.97 59.44
EDA 45.48±0.17 54.36±0.27 45.74±0.06 56.57±0.05 49.06±0.59 59.85±0.42 42.72 62.32 45.20 54.98
TEMP 41.46±0.24 47.42±0.36 41.85±0.19 48.67±0.21 41.19±0.24 49.39±0.23 40.89 58.96 38.97 44.32
|             | 57.13±0.86 | 63.34±1.00 | 66.33±0.36 | 76.17±0.42 | 64.24±0.39 | 73.62±0.55 |     |             |             |
| ----------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----------- | ----------- |
| Wristphysio |            |            |            |            |            |            |     | 58.18 68.85 | 50.85 58.54 |
Chest:
ECG 51.69±0.35 57.81±0.36 52.24±0.33 60.36±0.22 52.48±0.38 61.71±0.40 56.03 66.29 47.77 54.76
EDA 43.88±0.20 48.49±0.29 42.40±0.55 45.00±0.61 48.33±0.31 54.06±0.45 46.83 67.07 37.26 40.03
EMG 34.65±0.21 41.00±0.19 38.10±0.47 48.20±0.51 37.68±0.24 48.03±0.24 37.72 53.99 35.97 42.73
RESP 59.08±0.21 65.97±0.20 60.69±0.15 70.27±0.14 61.76±0.34 71.94±0.30 60.09 72.37 45.86 60.45
TEMP 41.27±0.29 47.53±0.28 42.46±0.24 48.40±0.26 40.76±0.8 47.98±0.60 30.96 55.68 35.18 43.32
|             | 55.10±0.92 | 58.62±1.07 | 64.60±0.54 | 71.37±0.58 | 72.51±0.17 | 80.34±0.43 |     |             |             |
| ----------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----------- | ----------- |
| Chestphysio |            |            |            |            |            |            |     | 74.43 79.35 | 51.09 57.31 |
Allwrist 43.62±1.33 53.98±1.79 62.86±0.65 74.85±0.20 64.12±0.98 75.21±0.77 63.24 70.74 37.20 45.54
Allchest 53.06±0.50 57.68±0.40 60.80±1.00 68.76±1.35 64.89±0.81 74.74±0.94 72.49 76.50 38.39 46.18
Allphysio 55.71±0.93 62.57±0.80 64.23±0.97 73.33±0.95 71.10±0.78 79.86±0.62 72.48 78.19 52.94 59.61
Allmodalities 58.05±1.61 63.56±1.73 64.08±1.68 74.97±1.11 68.85±0.89 79.57±0.93 71.56 75.80 48.70 56.14
| Baseline |     | RandomGuessing |     |          |     |          | Sophisticatedguessing |     |          |
| -------- | --- | -------------- | --- | -------- | --- | -------- | --------------------- | --- | -------- |
|          |     | F1-score       |     | Accuracy |     | F1-score |                       |     | Accuracy |
|          |     | 31.66          |     | 33.33    |     | 23.13    |                       |     | 53.12    |
Table4:Evaluationofthegivenmodalitiesandclassifiersonthebinary(stressvs.non-stress)classificationtask.
|     |     | DT  |     | RF  |     | AB  |     | LDA | kNN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F1-score Accuracy F1-score Accuracy F1-score Accuracy F1-score Accuracy F1-score Accuracy
Motion:
ACCwrist 55.36±0.47 64.08±0.49 59.02±0.78 69.96±0.55 61.70±0.80 71.69±0.45 44.93 60.02 52.72 63.80
ACCchest 61.92±0.83 71.75±0.53 59.91±0.25 72.87±0.08 62.17±0.45 73.87±0.30 57.52 72.05 47.79 57.81
Wrist:
|     | 78.27±0.17 | 81.39±0.15 | 81.35±0.15 | 84.18±0.11 | 81.23±0.15 | 84.10±0.13 |     |             |             |
| --- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----------- | ----------- |
| BVP |            |            |            |            |            |            |     | 83.08 85.83 | 78.94 82.06 |
EDAwrist 70.95±0.37 76.21±0.27 70.88±0.20 76.29±0.14 75.34±0.57 79.71±0.43 69.86 78.08 68.30 73.13
TEMPwrist 63.15±0.18 68.22±0.19 62.90±0.10 67.82±0.11 62.27±0.25 67.11±0.34 56.37 69.24 60.18 64.46
Wristphysio 82.37±0.21 84.88±0.11 86.10±0.29 88.33±0.25 85.86±0.20 88.05±0.18 83.77 86.46 78.93 81.96
Chest:
ECG 77.01±0.37 80.17±0.29 79.64±0.15 82.78±0.11 80.20±0.25 83.37±0.20 81.31 85.44 75.39 79.19
69.88±0.41 73.55±0.44 73.63±0.18 77.51±0.23 71.97±0.26 75.50±0.29 74.51 81.70 66.64 69.73
EDAchest
|     | 47.06±0.20 | 56.25±0.05 | 49.42±0.35 | 63.44±0.18 | 50.84±0.44 | 62.88±0.31 |     |             |             |
| --- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----------- | ----------- |
| EMG |            |            |            |            |            |            |     | 52.49 67.10 | 51.84 58.74 |
RESP 79.92±0.19 83.03±0.17 84.33±0.10 86.63±0.08 84.64±0.06 86.87±0.06 85.61 88.09 69.17 75.67
TEMPchest 57.40±0.08 64.33±0.07 56.75±0.25 64.75±0.28 55.03±0.27 63.46±0.21 41.00 69.49 51.64 58.25
Chestphysio 81.29±0.22 84.18±0.20 90.44±0.66 92.01±0.51 87.11±0.57 89.76±0.48 91.47 93.12 77.27 81.05
Allwrist 78.71±0.53 82.19±0.44 84.11±0.31 87.12±0.24 80.11±0.93 83.98±0.75 84.05 86.88 52.72 63.80
Allchest 78.26±0.46 81.29±0.38 90.04±0.84 91.70±0.75 89.57±0.61 91.58±0.46 91.07 92.83 64.20 69.70
|               | 83.03±1.61 | 85.16±1.50     | 86.02±0.55 | 87.91±0.54 | 87.78±1.38 | 89.77±1.17 |                       |             |             |
| ------------- | ---------- | -------------- | ---------- | ---------- | ---------- | ---------- | --------------------- | ----------- | ----------- |
| Allphysio     |            |                |            |            |            |            |                       | 90.93 92.51 | 79.44 83.16 |
|               | 80.83±1.13 | 83.60±1.08     | 85.71±0.63 | 87.74±0.60 | 83.88±0.93 | 87.00±0.78 |                       |             |             |
| Allmodalities |            |                |            |            |            |            |                       | 90.74 92.28 | 69.14 74.20 |
| Baseline      |            | RandomGuessing |            |            |            |            | Sophisticatedguessing |             |             |
|               |            | F1-score       |            | Accuracy   |            | F1-score   |                       |             | Accuracy    |
|               |            | 47.96          |            | 50.00      |            | 41.15      |                       |             | 69.94       |

Table5:Confusionmatrixofthebestsetuptrainedonthe Table6:Featureimportanceforthethree-classandbinary
three-classproblem. classificationtaskconsideringallmodalities.
True Baseline Stress Amusement Importance Three-class Importance BinaryTask
|     | Estimated |     |       |       |      |     |      | σRESP,chest  |      | σRESP,chest  |
| --- | --------- | --- | ----- | ----- | ---- | --- | ---- | ------------ | ---- | ------------ |
|     |           |     |       |       |      |     | 0.23 | E            | 0.35 | E            |
|     | Baseline  |     | 64577 | 1408  | 4444 |     |      |              |      |              |
|     |           |     |       |       |      |     | 0.11 | µ EC G,chest | 0.20 | µ EC G,chest |
|     | Stress    |     | 3968  | 34997 | 899  |     |      | H R          |      | H R          |
|     |           |     |       |       |      |     | 0.07 | min w ri st  | 0.09 | max w r ist  |
|     | Amusement |     | 12153 | 2374  | 7773 |     |      | T E M P      |      | T E M P      |
|     |           |     |       |       |      |     |      | ch e s t     |      | w ri st      |
|     |           |     |       |       |      |     | 0.06 | µ A C C , 3D | 0.07 | ranдe E D A  |
|     |           |     |       |       |      |     | 0.05 | ranдewrist   | 0.05 | #chest       |
|     |           |     |       |       |      |     |      | EDA          |      | SCR          |
modalities(three-classaccuracy:76%,binaryaccuracy:88%).When
bothwrist-andchest-basedphysiologicalmodalitiesarecombined,
anaccuracyof79%/92%isreachedforthethree-class/binaryprob-
| lem, | respectively. | This | is no | improvement | compared | to results |     |     |     |     |
| ---- | ------------- | ---- | ----- | ----------- | -------- | ---------- | --- | --- | --- | --- |
achievedusingonlythechest-basedphysiologicalmodalities.This 6 CONCLUSION
indicatesthatifthechest-basedmodalitiesareavailable,thewrist-
WepresentedWESAD,amultimodaldatasetforwearablestress
basedmodalitiesbecomeredundant.Nevertheless,theclassification andaffectdetection.Incontrasttootheravailabledatasets,WE-
scoresreachedusingonlythephysiologicalwrist-basedmodalities SADfeaturesallphysiologicalmodalitiescommonlyintegratedin
arepromising,especiallyconsideringtheminimalintrusivenature
commercialandmedicaldevices:bloodvolumepulse(BVP),electro-
ofthedeviceused.
cardiogram(ECG),electrodermalactivity(EDA),electromyogram
Overall,thebestperformanceresult(intermsofaccuracy)on
(EMG),respiration(RESP),bodytemperature(TEMP),andthree-
eachoftheclassificationtaskis: axisacceleration(ACC).Byusingthesemodalities,wehopethat
• 80.34%(three-classproblem,usingallchest-basedphysio- ourdatasetwillenableandsupportthedevelopmentofnewaffect
logicalmodalities,ABclassifier)
recognitionsystems.Thestudyprotocolaimedatinducingthree
|     | • 93.12% | (binary | case, using | all chest-based | physiological |     |     |     |     |     |
| --- | -------- | ------- | ----------- | --------------- | ------------- | --- | --- | --- | --- | --- |
differentaffectivestates(neutral,stress,amusement).Self-reports
modalities,LDAclassifier) onthesestateswerecollectedfromthestudyparticipants.
TheseresultsarecomparabletotheworkofGjoreskietal.[5], Forbenchmarking,weusedstandardphysiologicalandmotion
whoreportedanaccuracyof72%onathree-classproblem(no,low, featuresandcommonmachinelearningmethods.Onathree-class
andhighstress)andanaccuracyof83%inthebinarycase.InTable5 (baselinevs.stressvs.amusement)problemweachievedclassifica-
theconfusionmatrixofthebestclassifiertrainedonthethree-class tionaccuraciesofupto80%.Consideringabinaryclassification
classificationproblemisdisplayed.Thevaluesindicatethatthe problem(stressvs.non-stress),accuraciesofupto93%werereached.
classifierwasabletodistinguishwellbetweenthebaselineandthe Theseresultsshouldbeinterpretedwithcautionduetothelimi-
stressclass.However,distinguishingbetweentheclassesbaseline tationsofWESAD,regardingthenumberofsubjectsandthelack
andamusementwasdifficult.Theexplanationforthisistwofold. ofageandgenderdiversity.Nevertheless,sinceusingtheLOSO
First,thephysiologicalchangeselicitedbyamusementaresubtle. evaluationscheme,ourresultsindicatethatgeneralisationispossi-
Second, the self-reports indicate (see Table 2) that the subjects’ ble.Wealsoperformedadetailedanalysisontheimportanceofthe
affective state was less influenced by the amusement condition twodevicelocationsaswellasthedifferentsensormodalities.Our
comparedtothestresscondition. resultssuggestthatachest-baseddeviceleadstotheoverallbest
UsingallphysiologicalfeaturesandtheLDAclassifier,thesubject- classificationresultsandbyaddingdataofawrist-baseddeviceno
specificaccuraciesrangefrom69%to98%andfrom82%to100%,in
furtherimprovementisachieved.However,theresultsobtainedus-
thethree-classclassificationproblemandthebinarycase,respec- ingonlyawrist-baseddevicearepromising,especiallyconsidering
tively.However,onlyweakcorrelationswerefoundbetweenthe theminimalintrusivenatureofsuchadevice.
subject-specificaccuraciesandtheself-reportvalue(e.g.arousal/va- Furtherworkisrequiredtotaketheself-reportsintoaccount.
lence)differencesbetweenthevariousaffectivestates.Nevertheless, These self-reports could be used to create personalised models
thelargeinter-subjectdifferencesemphasisetheneedforpersonal-
whichareabletopredicttheaffectivestateofaspecificperson.
isationmethods. Moreover,themeditationperiodcouldbeaddedasanadditional
Inordertoassessthefeatureimportance,adecisiontreewas class,posingafour-classclassificationproblem.Thedatasetintro-
trainedforboththethree-classandthebinaryclassificationtask, ducedinthispaperispubliclyavailable,andcanbedownloaded
usingallavailablesensormodalitiesasinput.Thefeatureimpor- fromhttps://ubicomp.eti.uni-siegen.de/home/datasets/icmi18/.We
tanceiscomputedaccordingtotheGiniimportance(whichreflects invitetheresearchcommunitytoconsideritforalgorithmdevelop-
thereductionoftheGinicriterionbroughtbythefeatureunder mentandbenchmarking.
consideration).TheresultsofthisexperimentaredisplayedinTa-
| ble 6. | In both | cases (three-classes |     | and | binary classification) | the |     |     |     |     |
| ------ | ------- | -------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENT
| twomostimportantfeatures(σRESP, |     |     |     | ,andµECG)werealike.This |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
|                                 |     |     |     | E                       | HR  |     |     |     |     |     |
WewouldliketothankRahelMillaandEstherBoschformanyfruit-
suggeststhattheclassifierinthethree-classproblemfirstlearned
fuldiscussions.Furthermore,wethankallthestudyparticipants
todistinguishbetweenstressandnon-stressstates,beforeitlearned
fortheirparticipation.
toclassifythebaselineandamusementclasses.

REFERENCES
ConferenceonAcoustics,SpeechandSignalProcessing(ICASSP).2227–2231.
[1] 2016. HSEonworkrelatedstress. http://www.hse.gov.uk/statistics/causdis/- [18] A.Muaremi,B.Arnrich,andG.Tröster.2013.Towardsmeasuringstresswith
ffstress/index.htm.(2016). Accessed:2017-09-06. smartphonesandwearabledevicesduringworkdayandsleep.BioNanoScience3,
[2] B.Barker,H.Barker,andA.Wadsworth.1977.Factoranalysisoftheitemsofthe 2(2013),172–183.
state-traitanxietyinventory.JournalofClinicalPsychology33,2(1977),450–455. [19] R.Picard,E.Vyzas,andJ.Healey.2001.Towardmachineemotionalintelligence:
[3] J.Choi,B.Ahmed,andR.Gutierrez-Osuna.2012.Developmentandevaluation Analysisofaffectivephysiologicalstate.IEEETransactionsonPatternAnalysis
ofanambulatorystressmonitorbasedonwearablesensors.IEEETransactions andMachineIntelligence23,10(2001),1175–1191.
onInformationTechnologyinBiomedicine16,2(2012). [20] K.Plarre,A.Raij,andM.Scott.2011. Continuousinferenceofpsychological
[4] G.ChrousosandP.Gold.1992.Theconceptsofstressandstresssystemdisorders: stressfromsensorymeasurementscollectedinthenaturalenvironment.In10th
overviewofphysicalandbehavioralhomeostasis.Jama267,9(1992),1244–1252. InternationalConferenceonInformationProcessinginSensorNetworks(IPSN).
[5] M.Gjoreski,H.Gjoreski,andM.Gams.2016.Continuousstressdetectionusing 97–108.
awristdevice:Inlaboratoryandreallife.InUbiComp’16.1185–1193. [21] A.ReissandD.Stricker.2012. Introducinganewbenchmarkeddatasetfor
[6] J.HealeyandR.Picard.2005.Detectingstressduringreal-worlddrivingtasks activitymonitoring.In16thInternationalSymposiumonWearableComputers
usingphysiologicalsensors. IEEETransactionsonIntelligentTransportation (ISWC).108–109.
Systems6,2(2005),156–166. [22] R.RosmondandP.Björntorp.1998.Endocrineandmetabolicaberrationsinmen
[7] W.HeltonandK.Näswall.2015. Shortstressstatequestionnaire. European withabdominalobesityinrelationtoanxio-depressiveinfirmity.Metabolism47,
JournalofPsychologicalAssessment(2015). 10(1998),1187–1193.
[8] K.Hovsepian,M.al’Absi,andS.Kumar.2015.cStress:Towardsagoldstandard [23] J.Russell.1979.Affectivespaceisbipolar.AmericanPsychologicalAssociation.
forcontinuousstressassessmentinthemobileenvironment.InUbiComp’15. [24] A.Samson,S.Kreibig,andJ.Gross.2016.Elicitingpositive,negativeandmixed
493–504. emotionalstates:Afilmlibraryforaffectivescientists.CognitionandEmotion30,
[9] A.JohnsonandE.Anderson.1990.Stressandarousal.(1990). 5(2016),827–856.
[10] J.KimandE.André.2008.Emotionrecognitionbasedonphysiologicalchanges [25] H.Selye.1976.Stresswithoutdistress.InPsychopathologyofHumanAdaptation.
inmusiclistening.IEEETransactionsonPatternAnalysisandMachineIntelligence 137–146.
30,12(2008),2067–2083. [26] C.Setz,B.Arnrich,J.Schumm,R.LaMarca,G.Tröster,andU.Ehlert.2010.
[11] C.Kirschbaum,K.Pirke,andD.Hellhammer.1993.TheTrierSocialStressTest– DiscriminatingstressfromcognitiveloadusingawearableEDAdevice.IEEE
atoolforinvestigatingpsychobiologicalstressresponsesinalaboratorysetting. TransactionsonInformationTechnologyinBiomedicine14,2(2010),410–417.
Neuropsychobiology28,1-2(1993),76–81. [27] F.-T.Sun,C.Kuo,H.-T.Cheng,S.Buthpitiya,P.Collins,andM.Griss.2012.
[12] S.Koelstra,C.Muhl,andI.Patras.2012.Deap:Adatabaseforemotionanalysis; Activity-awarementalstressdetectionusingphysiologicalsensors.InMobile
usingphysiologicalsignals.IEEETransactionsonAffectiveComputing3,1(2012), Computing,Applications,andServices.211–230.
18–31. [28] N.A.TaylorandC.A.Machado-Moreira.2013.Regionalvariationsintransepider-
[13] S.Kreibig.2010. Autonomicnervoussystemactivityinemotion:Areview. malwaterloss,eccrinesweatglanddensity,sweatsecretionratesandelectrolyte
BiologicalPsychology84,3(2010),394–421. compositioninrestingandexercisinghumans.ExtremePhysiology&Medicine2,
[14] H.Lu,D.Frauendorfer,andT.Choudhury.2012.StressSense:Detectingstress 4(2013).
[29] P.Tzirakis,G.Trigeorgis,andS.Zafeiriou.2017.End-to-endmultimodalemotion
inunconstrainedacousticenvironmentsusingsmartphones.InUbiComp’12.
recognitionusingdeepneuralnetworks.CoRR(2017).
351–360.
[30] D.Watson,L.Clark,andA.Tellegen.1988.Developmentandvalidationofbrief
[15] M.Malik.1996.TaskforceoftheEuropeansocietyofcardiologyandthenorth
measuresofpositiveandnegativeaffect:thePANASscales.JournalofPersonality
Americansocietyofpacingandelectrophysiology.Heartratevariability.Stan-
andSocialPsychology54,6(1988),1063.
dardsofmeasurement,physiologicalinterpretation,andclinicaluse.EurHeartJ.
[31] J.Wijsman,B.Grundlehner,andH.Hermens.2010.TrapeziusmuscleEMGas
17(1996),354–381.
predictorofmentalstress.InWirelessHealth2010(WH’10).155–163.
[16] B.McEwenandE.Stellar.1993.Stressandtheindividual:mechanismsleadingto
[32] A.Zenonos,A.Khan,andM.Sooriyabandara.2016.HealthyOffice:Moodrecog-
disease.ArchivesofInternalMedicine153,18(1993),2093–2101.
nitionatworkusingsmartphonesandwearablesensors.InPerComWorkshops.
[17] S.Mirsamadi,E.Barsoum,andC.Zhang.2017.Automaticspeechemotionrecog-
nitionusingrecurrentneuralnetworkswithlocalattention.InIEEEInternational