from src import MyPymysqlPool

mysql = MyPymysqlPool()

datas = """
100000000   中国  zg  zhongguo
100110000   北京市 bj  beijing
100110100   市辖区 sxq shixiaqu
100110101   东城区 dcq dongchengqu
100110102   西城区 xcq xichengqu
100110105   朝阳区 cyq chaoyangqu
100110106   丰台区 ftq fengtaiqu
100110107   石景山区    sjsq    shijingshanqu
100110108   海淀区 hdq haidianqu
100110109   门头沟区    mtgq    mentougouqu
100110111   房山区 fsq fangshanqu
100110112   通州区 tzq tongzhouqu
100110113   顺义区 syq shunyiqu
100110114   昌平区 cpq changpingqu
100110115   大兴区 dxq daxingqu
100110116   怀柔区 hrq huairouqu
100110117   平谷区 pgq pingguqu
100110200   县   x   xian
100110228   密云县 myx miyunxian
100110229   延庆县 yqx yanqingxian
100120000   天津市 tj  tianjin
100120100   市辖区 sxq shixiaqu
100120101   和平区 hpq hepingqu
100120102   河东区 hdq hedongqu
100120103   河西区 hxq hexiqu
100120104   南开区 nkq nankaiqu
100120105   河北区 hbq hebeiqu
100120106   红桥区 hqq hongqiaoqu
100120110   东丽区 dlq dongliqu
100120111   西青区 xqq xiqingqu
100120112   津南区 jnq jinnanqu
100120113   北辰区 bcq beichenqu
100120114   武清区 wqq wuqingqu
100120115   宝坻区 bcq baochiqu
100120116   滨海新区    bhxq    binhaixinqu
100120200   县   x   xian
100120221   宁河县 nhx ninghexian
100120223   静海县 jhx jinghaixian
100120225   蓟县  jx  jixian
100130000   河北省 hbs hebeisheng
100130100   石家庄市    sjzs    shijiazhuangshi
100130101   市辖区 sxq shixiaqu
100130102   长安区 zaq zhanganqu
100130104   桥西区 qxq qiaoxiqu
100130105   新华区 xhq xinhuaqu
100130107   井陉矿区    jxkq    jingxingkuangqu
100130108   裕华区 yhq yuhuaqu
100130109   藁城区 gcq gaochengqu
100130110   鹿泉区 lqq luquanqu
100130111   栾城区 lcq luanchengqu
100130121   井陉县 jxx jingxingxian
100130123   正定县 zdx zhengdingxian
100130125   行唐县 xtx xingtangxian
100130126   灵寿县 lsx lingshouxian
100130127   高邑县 gyx gaoyixian
100130128   深泽县 szx shenzexian
100130129   赞皇县 zhx zanhuangxian
100130130   无极县 wjx wujixian
100130131   平山县 psx pingshanxian
100130132   元氏县 ysx yuanshixian
100130133   赵县  zx  zhaoxian
100130181   辛集市 xjs xinjishi
100130183   晋州市 jzs jinzhoushi
100130184   新乐市 xls xinleshi
100130200   唐山市 tss tangshanshi
100130201   市辖区 sxq shixiaqu
100130202   路南区 lnq lunanqu
100130203   路北区 lbq lubeiqu
100130204   古冶区 gyq guyequ
100130205   开平区 kpq kaipingqu
100130207   丰南区 fnq fengnanqu
100130208   丰润区 frq fengrunqu
100130209   曹妃甸区    cfdq    caofeidianqu
100130223   滦县  lx  luanxian
100130224   滦南县 lnx luannanxian
100130225   乐亭县 ltx letingxian
100130227   迁西县 qxx qianxixian
100130229   玉田县 ytx yutianxian
100130281   遵化市 zhs zunhuashi
100130283   迁安市 qas qiananshi
100130300   秦皇岛市    qhds    qinhuangdaoshi
100130301   市辖区 sxq shixiaqu
100130302   海港区 hgq haigangqu
100130303   山海关区    shgq    shanhaiguanqu
100130304   北戴河区    bdhq    beidaihequ
100130321   青龙满族自治县 qlmzzzx qinglongmanzuzizhixian
100130322   昌黎县 clx changlixian
100130323   抚宁县 fnx funingxian
100130324   卢龙县 llx lulongxian
100130400   邯郸市 hds handanshi
100130401   市辖区 sxq shixiaqu
100130402   邯山区 hsq hanshanqu
100130403   丛台区 ctq congtaiqu
100130404   复兴区 fxq fuxingqu
100130406   峰峰矿区    ffkq    fengfengkuangqu
100130421   邯郸县 hdx handanxian
100130423   临漳县 lzx linzhangxian
100130424   成安县 cax chenganxian
100130425   大名县 dmx damingxian
100130426   涉县  sx  shexian
100130427   磁县  cx  cixian
100130428   肥乡县 fxx feixiangxian
100130429   永年县 ynx yongnianxian
100130430   邱县  qx  qiuxian
100130431   鸡泽县 jzx jizexian
100130432   广平县 gpx guangpingxian
100130433   馆陶县 gtx guantaoxian
100130434   魏县  wx  weixian
100130435   曲周县 qzx quzhouxian
100130481   武安市 was wuanshi
100130500   邢台市 xts xingtaishi
100130501   市辖区 sxq shixiaqu
100130502   桥东区 qdq qiaodongqu
100130503   桥西区 qxq qiaoxiqu
100130521   邢台县 xtx xingtaixian
100130522   临城县 lcx linchengxian
100130523   内丘县 nqx neiqiuxian
100130524   柏乡县 bxx boxiangxian
100130525   隆尧县 lyx longyaoxian
100130526   任县  rx  renxian
100130527   南和县 nhx nanhexian
100130528   宁晋县 njx ningjinxian
100130529   巨鹿县 jlx juluxian
100130530   新河县 xhx xinhexian
100130531   广宗县 gzx guangzongxian
100130532   平乡县 pxx pingxiangxian
100130533   威县  wx  weixian
100130534   清河县 qhx qinghexian
100130535   临西县 lxx linxixian
100130581   南宫市 ngs nangongshi
100130582   沙河市 shs shaheshi
100130600   保定市 bds baodingshi
100130601   市辖区 sxq shixiaqu
100130602   新市区 xsq xinshiqu
100130603   北市区 bsq beishiqu
100130604   南市区 nsq nanshiqu
100130621   满城县 mcx manchengxian
100130622   清苑县 qyx qingyuanxian
100130623   涞水县 lsx laishuixian
100130624   阜平县 fpx fupingxian
100130625   徐水县 xsx xushuixian
100130626   定兴县 dxx dingxingxian
100130627   唐县  tx  tangxian
100130628   高阳县 gyx gaoyangxian
100130629   容城县 rcx rongchengxian
100130630   涞源县 lyx laiyuanxian
100130631   望都县 wdx wangdouxian
100130632   安新县 axx anxinxian
100130633   易县  yx  yixian
100130634   曲阳县 qyx quyangxian
100130635   蠡县  lx  lixian
100130636   顺平县 spx shunpingxian
100130637   博野县 byx boyexian
100130638   雄县  xx  xiongxian
100130681   涿州市 zzs zhuozhoushi
100130682   定州市 dzs dingzhoushi
100130683   安国市 ags anguoshi
100130684   高碑店市    gbds    gaobeidianshi
100130700   张家口市    zjks    zhangjiakoushi
100130701   市辖区 sxq shixiaqu
100130702   桥东区 qdq qiaodongqu
100130703   桥西区 qxq qiaoxiqu
100130705   宣化区 xhq xuanhuaqu
100130706   下花园区    xhyq    xiahuayuanqu
100130721   宣化县 xhx xuanhuaxian
100130722   张北县 zbx zhangbeixian
100130723   康保县 kbx kangbaoxian
100130724   沽源县 gyx guyuanxian
100130725   尚义县 syx shangyixian
100130726   蔚县  yx  yuxian
100130727   阳原县 yyx yangyuanxian
100130728   怀安县 hax huaianxian
100130729   万全县 wqx wanquanxian
100130730   怀来县 hlx huailaixian
100130731   涿鹿县 zlx zhuoluxian
100130732   赤城县 ccx chichengxian
100130733   崇礼县 clx chonglixian
100130800   承德市 cds chengdeshi
100130801   市辖区 sxq shixiaqu
100130802   双桥区 sqq shuangqiaoqu
100130803   双滦区 slq shuangluanqu
100130804   鹰手营子矿区  ysyzkq  yingshouyingzikuangqu
100130821   承德县 cdx chengdexian
100130822   兴隆县 xlx xinglongxian
100130823   平泉县 pqx pingquanxian
100130824   滦平县 lpx luanpingxian
100130825   隆化县 lhx longhuaxian
100130826   丰宁满族自治县 fnmzzzx fengningmanzuzizhixian
100130827   宽城满族自治县 kcmzzzx kuanchengmanzuzizhixian
100130828   围场满族蒙古族自治县  wcmzmgzzzx  weichangmanzumengguzuzizhixian
100130900   沧州市 czs cangzhoushi
100130901   市辖区 sxq shixiaqu
100130902   新华区 xhq xinhuaqu
100130903   运河区 yhq yunhequ
100130921   沧县  cx  cangxian
100130922   青县  qx  qingxian
100130923   东光县 dgx dongguangxian
100130924   海兴县 hxx haixingxian
100130925   盐山县 ysx yanshanxian
100130926   肃宁县 snx suningxian
100130927   南皮县 npx nanpixian
100130928   吴桥县 wqx wuqiaoxian
100130929   献县  xx  xianxian
100130930   孟村回族自治县 mchzzzx mengcunhuizuzizhixian
100130981   泊头市 bts botoushi
100130982   任丘市 rqs renqiushi
100130983   黄骅市 hhs huanghuashi
100130984   河间市 hjs hejianshi
100131000   廊坊市 lfs langfangshi
100131001   市辖区 sxq shixiaqu
100131002   安次区 acq anciqu
100131003   广阳区 gyq guangyangqu
100131022   固安县 gax guanxian
100131023   永清县 yqx yongqingxian
100131024   香河县 xhx xianghexian
100131025   大城县 dcx dachengxian
100131026   文安县 wax wenanxian
100131028   大厂回族自治县 dchzzzx dachanghuizuzizhixian
100131081   霸州市 bzs bazhoushi
100131082   三河市 shs sanheshi
100131100   衡水市 hss hengshuishi
100131101   市辖区 sxq shixiaqu
100131102   桃城区 tcq taochengqu
100131121   枣强县 zqx zaoqiangxian
100131122   武邑县 wyx wuyixian
100131123   武强县 wqx wuqiangxian
100131124   饶阳县 ryx raoyangxian
100131125   安平县 apx anpingxian
100131126   故城县 gcx guchengxian
100131127   景县  jx  jingxian
100131128   阜城县 fcx fuchengxian
100131181   冀州市 jzs jizhoushi
100131182   深州市 szs shenzhoushi
100140000   山西省 sxs shanxisheng
100140100   太原市 tys taiyuanshi
100140101   市辖区 sxq shixiaqu
100140105   小店区 xdq xiaodianqu
100140106   迎泽区 yzq yingzequ
100140107   杏花岭区    xhlq    xinghualingqu
100140108   尖草坪区    jcpq    jiancaopingqu
100140109   万柏林区    wblq    wanbolinqu
100140110   晋源区 jyq jinyuanqu
100140121   清徐县 qxx qingxuxian
100140122   阳曲县 yqx yangquxian
100140123   娄烦县 lfx loufanxian
100140181   古交市 gjs gujiaoshi
100140200   大同市 dts datongshi
100140201   市辖区 sxq shixiaqu
100140202   城区  cq  chengqu
100140203   矿区  kq  kuangqu
100140211   南郊区 njq nanjiaoqu
100140212   新荣区 xrq xinrongqu
100140221   阳高县 ygx yanggaoxian
100140222   天镇县 tzx tianzhenxian
100140223   广灵县 glx guanglingxian
100140224   灵丘县 lqx lingqiuxian
100140225   浑源县 hyx hunyuanxian
100140226   左云县 zyx zuoyunxian
100140227   大同县 dtx datongxian
100140300   阳泉市 yqs yangquanshi
100140301   市辖区 sxq shixiaqu
100140302   城区  cq  chengqu
100140303   矿区  kq  kuangqu
100140311   郊区  jq  jiaoqu
100140321   平定县 pdx pingdingxian
100140322   盂县  yx  yuxian
100140400   长治市 zzs zhangzhishi
100140401   市辖区 sxq shixiaqu
100140402   城区  cq  chengqu
100140411   郊区  jq  jiaoqu
100140421   长治县 zzx zhangzhixian
100140423   襄垣县 xyx xiangyuanxian
100140424   屯留县 tlx tunliuxian
100140425   平顺县 psx pingshunxian
100140426   黎城县 lcx lichengxian
100140427   壶关县 hgx huguanxian
100140428   长子县 zzx zhangzixian
100140429   武乡县 wxx wuxiangxian
100140430   沁县  qx  qinxian
100140431   沁源县 qyx qinyuanxian
100140481   潞城市 lcs luchengshi
100140500   晋城市 jcs jinchengshi
100140501   市辖区 sxq shixiaqu
100140502   城区  cq  chengqu
100140521   沁水县 qsx qinshuixian
100140522   阳城县 ycx yangchengxian
100140524   陵川县 lcx lingchuanxian
100140525   泽州县 zzx zezhouxian
100140581   高平市 gps gaopingshi
100140600   朔州市 szs shuozhoushi
100140601   市辖区 sxq shixiaqu
100140602   朔城区 scq shuochengqu
100140603   平鲁区 plq pingluqu
100140621   山阴县 syx shanyinxian
100140622   应县  yx  yingxian
100140623   右玉县 yyx youyuxian
100140624   怀仁县 hrx huairenxian
100140700   晋中市 jzs jinzhongshi
100140701   市辖区 sxq shixiaqu
100140702   榆次区 ycq yuciqu
100140721   榆社县 ysx yushexian
100140722   左权县 zqx zuoquanxian
100140723   和顺县 hsx heshunxian
100140724   昔阳县 xyx xiyangxian
100140725   寿阳县 syx shouyangxian
100140726   太谷县 tgx taiguxian
100140727   祁县  qx  qixian
100140728   平遥县 pyx pingyaoxian
100140729   灵石县 lsx lingshixian
100140781   介休市 jxs jiexiushi
100140800   运城市 ycs yunchengshi
100140801   市辖区 sxq shixiaqu
100140802   盐湖区 yhq yanhuqu
100140821   临猗县 lyx linyixian
100140822   万荣县 wrx wanrongxian
100140823   闻喜县 wxx wenxixian
100140824   稷山县 jsx jishanxian
100140825   新绛县 xjx xinjiangxian
100140826   绛县  jx  jiangxian
100140827   垣曲县 yqx yuanquxian
100140828   夏县  xx  xiaxian
100140829   平陆县 plx pingluxian
100140830   芮城县 rcx ruichengxian
100140881   永济市 yjs yongjishi
100140882   河津市 hjs hejinshi
100140900   忻州市 xzs xinzhoushi
100140901   市辖区 sxq shixiaqu
100140902   忻府区 xfq xinfuqu
100140921   定襄县 dxx dingxiangxian
100140922   五台县 wtx wutaixian
100140923   代县  dx  daixian
100140924   繁峙县 fzx fanzhixian
100140925   宁武县 nwx ningwuxian
100140926   静乐县 jlx jinglexian
100140927   神池县 scx shenchixian
100140928   五寨县 wzx wuzhaixian
100140929   岢岚县 klx kelanxian
100140930   河曲县 hqx hequxian
100140931   保德县 bdx baodexian
100140932   偏关县 pgx pianguanxian
100140981   原平市 yps yuanpingshi
100141000   临汾市 lfs linfenshi
100141001   市辖区 sxq shixiaqu
100141002   尧都区 ydq yaodouqu
100141021   曲沃县 qwx quwoxian
100141022   翼城县 ycx yichengxian
100141023   襄汾县 xfx xiangfenxian
100141024   洪洞县 hdx hongdongxian
100141025   古县  gx  guxian
100141026   安泽县 azx anzexian
100141027   浮山县 fsx fushanxian
100141028   吉县  jx  jixian
100141029   乡宁县 xnx xiangningxian
100141030   大宁县 dnx daningxian
100141031   隰县  xx  xixian
100141032   永和县 yhx yonghexian
100141033   蒲县  px  puxian
100141034   汾西县 fxx fenxixian
100141081   侯马市 hms houmashi
100141082   霍州市 hzs huozhoushi
100141100   吕梁市 lls lu:liangshi
100141101   市辖区 sxq shixiaqu
100141102   离石区 lsq lishiqu
100141121   文水县 wsx wenshuixian
100141122   交城县 jcx jiaochengxian
100141123   兴县  xx  xingxian
100141124   临县  lx  linxian
100141125   柳林县 llx liulinxian
100141126   石楼县 slx shilouxian
100141127   岚县  lx  lanxian
100141128   方山县 fsx fangshanxian
100141129   中阳县 zyx zhongyangxian
100141130   交口县 jkx jiaokouxian
100141181   孝义市 xys xiaoyishi
100141182   汾阳市 fys fenyangshi
100150000   内蒙古自治区  nmgzzq  neimengguzizhiqu
100150100   呼和浩特市   hhhts   huhehaoteshi
100150101   市辖区 sxq shixiaqu
100150102   新城区 xcq xinchengqu
100150103   回民区 hmq huiminqu
100150104   玉泉区 yqq yuquanqu
100150105   赛罕区 shq saihanqu
100150121   土默特左旗   tmtzq   tumotezuoqi
100150122   托克托县    tktx    tuoketuoxian
100150123   和林格尔县   hlgex   helingeerxian
100150124   清水河县    qshx    qingshuihexian
100150125   武川县 wcx wuchuanxian
100150200   包头市 bts baotoushi
100150201   市辖区 sxq shixiaqu
100150202   东河区 dhq donghequ
100150203   昆都仑区    kdlq    kundoulunqu
100150204   青山区 qsq qingshanqu
100150205   石拐区 sgq shiguaiqu
100150206   白云鄂博矿区  byebkq  baiyunebokuangqu
100150207   九原区 jyq jiuyuanqu
100150221   土默特右旗   tmtyq   tumoteyouqi
100150222   固阳县 gyx guyangxian
100150223   达尔罕茂明安联合旗   dehmmalhq   daerhanmaominganlianheqi
100150300   乌海市 whs wuhaishi
100150301   市辖区 sxq shixiaqu
100150302   海勃湾区    hbwq    haibowanqu
100150303   海南区 hnq hainanqu
100150304   乌达区 wdq wudaqu
100150400   赤峰市 cfs chifengshi
100150401   市辖区 sxq shixiaqu
100150402   红山区 hsq hongshanqu
100150403   元宝山区    ybsq    yuanbaoshanqu
100150404   松山区 ssq songshanqu
100150421   阿鲁科尔沁旗  alkeqq  alukeerqinqi
100150422   巴林左旗    blzq    balinzuoqi
100150423   巴林右旗    blyq    balinyouqi
100150424   林西县 lxx linxixian
100150425   克什克腾旗   ksktq   keshenketengqi
100150426   翁牛特旗    wntq    wengniuteqi
100150428   喀喇沁旗    klqq    kalaqinqi
100150429   宁城县 ncx ningchengxian
100150430   敖汉旗 ahq aohanqi
100150500   通辽市 tls tongliaoshi
100150501   市辖区 sxq shixiaqu
100150502   科尔沁区    keqq    keerqinqu
100150521   科尔沁左翼中旗 keqzyzq keerqinzuoyizhongqi
100150522   科尔沁左翼后旗 keqzyhq keerqinzuoyihouqi
100150523   开鲁县 klx kailuxian
100150524   库伦旗 klq kulunqi
100150525   奈曼旗 nmq naimanqi
100150526   扎鲁特旗    zltq    zhaluteqi
100150581   霍林郭勒市   hlgls   huolinguoleshi
100150600   鄂尔多斯市   eedss   eerduosishi
100150601   市辖区 sxq shixiaqu
100150602   东胜区 dsq dongshengqu
100150621   达拉特旗    dltq    dalateqi
100150622   准格尔旗    zgeq    zhungeerqi
100150623   鄂托克前旗   etkqq   etuokeqianqi
100150624   鄂托克旗    etkq    etuokeqi
100150625   杭锦旗 hjq hangjinqi
100150626   乌审旗 wsq wushenqi
100150627   伊金霍洛旗   yjhlq   yijinhuoluoqi
100150700   呼伦贝尔市   hlbes   hulunbeiershi
100150701   市辖区 sxq shixiaqu
100150702   海拉尔区    hleq    hailaerqu
100150703   扎赉诺尔区   zlneq   zhalainuoerqu
100150721   阿荣旗 arq arongqi
100150722   莫力达瓦达斡尔族自治旗 mldwdwezzzq molidawadawoerzuzizhiqi
100150723   鄂伦春自治旗  elczzq  elunchunzizhiqi
100150724   鄂温克族自治旗 ewkzzzq ewenkezuzizhiqi
100150725   陈巴尔虎旗   cbehq   chenbaerhuqi
100150726   新巴尔虎左旗  xbehzq  xinbaerhuzuoqi
100150727   新巴尔虎右旗  xbehyq  xinbaerhuyouqi
100150781   满洲里市    mzls    manzhoulishi
100150782   牙克石市    ykss    yakeshishi
100150783   扎兰屯市    zlts    zhalantunshi
100150784   额尔古纳市   eegns   eergunashi
100150785   根河市 ghs genheshi
100150800   巴彦淖尔市   bynes   bayannaoershi
100150801   市辖区 sxq shixiaqu
100150802   临河区 lhq linhequ
100150821   五原县 wyx wuyuanxian
100150822   磴口县 dkx dengkouxian
100150823   乌拉特前旗   wltqq   wulateqianqi
100150824   乌拉特中旗   wltzq   wulatezhongqi
100150825   乌拉特后旗   wlthq   wulatehouqi
100150826   杭锦后旗    hjhq    hangjinhouqi
100150900   乌兰察布市   wlcbs   wulanchabushi
100150901   市辖区 sxq shixiaqu
100150902   集宁区 jnq jiningqu
100150921   卓资县 zzx zhuozixian
100150922   化德县 hdx huadexian
100150923   商都县 sdx shangdouxian
100150924   兴和县 xhx xinghexian
100150925   凉城县 lcx liangchengxian
100150926   察哈尔右翼前旗 cheyyqq chahaeryouyiqianqi
100150927   察哈尔右翼中旗 cheyyzq chahaeryouyizhongqi
100150928   察哈尔右翼后旗 cheyyhq chahaeryouyihouqi
100150929   四子王旗    szwq    siziwangqi
100150981   丰镇市 fzs fengzhenshi
100152200   兴安盟 xam xinganmeng
100152201   乌兰浩特市   wlhts   wulanhaoteshi
100152202   阿尔山市    aess    aershanshi
100152221   科尔沁右翼前旗 keqyyqq keerqinyouyiqianqi
100152222   科尔沁右翼中旗 keqyyzq keerqinyouyizhongqi
100152223   扎赉特旗    zltq    zhalaiteqi
100152224   突泉县 tqx tuquanxian
100152500   锡林郭勒盟   xlglm   xilinguolemeng
100152501   二连浩特市   elhts   erlianhaoteshi
100152502   锡林浩特市   xlhts   xilinhaoteshi
100152522   阿巴嘎旗    abgq    abagaqi
100152523   苏尼特左旗   sntzq   sunitezuoqi
100152524   苏尼特右旗   sntyq   suniteyouqi
100152525   东乌珠穆沁旗  dwzmqq  dongwuzhumuqinqi
100152526   西乌珠穆沁旗  xwzmqq  xiwuzhumuqinqi
100152527   太仆寺旗    tpsq    taipusiqi
100152528   镶黄旗 xhq xianghuangqi
100152529   正镶白旗    zxbq    zhengxiangbaiqi
100152530   正蓝旗 zlq zhenglanqi
100152531   多伦县 dlx duolunxian
100152900   阿拉善盟    alsm    alashanmeng
100152921   阿拉善左旗   alszq   alashanzuoqi
100152922   阿拉善右旗   alsyq   alashanyouqi
100152923   额济纳旗    ejnq    ejinaqi
100210000   辽宁省 lns liaoningsheng
100210100   沈阳市 sys shenyangshi
100210101   市辖区 sxq shixiaqu
100210102   和平区 hpq hepingqu
100210103   沈河区 shq shenhequ
100210104   大东区 ddq dadongqu
100210105   皇姑区 hgq huangguqu
100210106   铁西区 txq tiexiqu
100210111   苏家屯区    sjtq    sujiatunqu
100210112   浑南区 hnq hunnanqu
100210113   沈北新区    sbxq    shenbeixinqu
100210114   于洪区 yhq yuhongqu
100210122   辽中县 lzx liaozhongxian
100210123   康平县 kpx kangpingxian
100210124   法库县 fkx fakuxian
100210181   新民市 xms xinminshi
100210200   大连市 dls dalianshi
100210201   市辖区 sxq shixiaqu
100210202   中山区 zsq zhongshanqu
100210203   西岗区 xgq xigangqu
100210204   沙河口区    shkq    shahekouqu
100210211   甘井子区    gjzq    ganjingziqu
100210212   旅顺口区    lskq    lu:shunkouqu
100210213   金州区 jzq jinzhouqu
100210224   长海县 zhx zhanghaixian
100210281   瓦房店市    wfds    wafangdianshi
100210282   普兰店市    plds    pulandianshi
100210283   庄河市 zhs zhuangheshi
100210300   鞍山市 ass anshanshi
100210301   市辖区 sxq shixiaqu
100210302   铁东区 tdq tiedongqu
100210303   铁西区 txq tiexiqu
100210304   立山区 lsq lishanqu
100210311   千山区 qsq qianshanqu
100210321   台安县 tax taianxian
100210323   岫岩满族自治县 xymzzzx xiuyanmanzuzizhixian
100210381   海城市 hcs haichengshi
100210400   抚顺市 fss fushunshi
100210401   市辖区 sxq shixiaqu
100210402   新抚区 xfq xinfuqu
100210403   东洲区 dzq dongzhouqu
100210404   望花区 whq wanghuaqu
100210411   顺城区 scq shunchengqu
100210421   抚顺县 fsx fushunxian
100210422   新宾满族自治县 xbmzzzx xinbinmanzuzizhixian
100210423   清原满族自治县 qymzzzx qingyuanmanzuzizhixian
100210500   本溪市 bxs benxishi
100210501   市辖区 sxq shixiaqu
100210502   平山区 psq pingshanqu
100210503   溪湖区 xhq xihuqu
100210504   明山区 msq mingshanqu
100210505   南芬区 nfq nanfenqu
100210521   本溪满族自治县 bxmzzzx benximanzuzizhixian
100210522   桓仁满族自治县 hrmzzzx huanrenmanzuzizhixian
100210600   丹东市 dds dandongshi
100210601   市辖区 sxq shixiaqu
100210602   元宝区 ybq yuanbaoqu
100210603   振兴区 zxq zhenxingqu
100210604   振安区 zaq zhenanqu
100210624   宽甸满族自治县 kdmzzzx kuandianmanzuzizhixian
100210681   东港市 dgs donggangshi
100210682   凤城市 fcs fengchengshi
100210700   锦州市 jzs jinzhoushi
100210701   市辖区 sxq shixiaqu
100210702   古塔区 gtq gutaqu
100210703   凌河区 lhq linghequ
100210711   太和区 thq taihequ
100210726   黑山县 hsx heishanxian
100210727   义县  yx  yixian
100210781   凌海市 lhs linghaishi
100210782   北镇市 bzs beizhenshi
100210800   营口市 yks yingkoushi
100210801   市辖区 sxq shixiaqu
100210802   站前区 zqq zhanqianqu
100210803   西市区 xsq xishiqu
100210804   鲅鱼圈区    byqq    bayuquanqu
100210811   老边区 lbq laobianqu
100210881   盖州市 gzs gaizhoushi
100210882   大石桥市    dsqs    dashiqiaoshi
100210900   阜新市 fxs fuxinshi
100210901   市辖区 sxq shixiaqu
100210902   海州区 hzq haizhouqu
100210903   新邱区 xqq xinqiuqu
100210904   太平区 tpq taipingqu
100210905   清河门区    qhmq    qinghemenqu
100210911   细河区 xhq xihequ
100210921   阜新蒙古族自治县    fxmgzzzx    fuxinmengguzuzizhixian
100210922   彰武县 zwx zhangwuxian
100211000   辽阳市 lys liaoyangshi
100211001   市辖区 sxq shixiaqu
100211002   白塔区 btq baitaqu
100211003   文圣区 wsq wenshengqu
100211004   宏伟区 hwq hongweiqu
100211005   弓长岭区    gzlq    gongzhanglingqu
100211011   太子河区    tzhq    taizihequ
100211021   辽阳县 lyx liaoyangxian
100211081   灯塔市 dts dengtashi
100211100   盘锦市 pjs panjinshi
100211101   市辖区 sxq shixiaqu
100211102   双台子区    stzq    shuangtaiziqu
100211103   兴隆台区    xltq    xinglongtaiqu
100211121   大洼县 dwx dawaxian
100211122   盘山县 psx panshanxian
100211200   铁岭市 tls tielingshi
100211201   市辖区 sxq shixiaqu
100211202   银州区 yzq yinzhouqu
100211204   清河区 qhq qinghequ
100211221   铁岭县 tlx tielingxian
100211223   西丰县 xfx xifengxian
100211224   昌图县 ctx changtuxian
100211281   调兵山市    dbss    diaobingshanshi
100211282   开原市 kys kaiyuanshi
100211300   朝阳市 cys chaoyangshi
100211301   市辖区 sxq shixiaqu
100211302   双塔区 stq shuangtaqu
100211303   龙城区 lcq longchengqu
100211321   朝阳县 cyx chaoyangxian
100211322   建平县 jpx jianpingxian
100211324   喀喇沁左翼蒙古族自治县 klqzymgzzzx kalaqinzuoyimengguzuzizhixian
100211381   北票市 bps beipiaoshi
100211382   凌源市 lys lingyuanshi
100211400   葫芦岛市    hlds    huludaoshi
100211401   市辖区 sxq shixiaqu
100211402   连山区 lsq lianshanqu
100211403   龙港区 lgq longgangqu
100211404   南票区 npq nanpiaoqu
100211421   绥中县 szx suizhongxian
100211422   建昌县 jcx jianchangxian
100211481   兴城市 xcs xingchengshi
100220000   吉林省 jls jilinsheng
100220100   长春市 zcs zhangchunshi
100220101   市辖区 sxq shixiaqu
100220102   南关区 ngq nanguanqu
100220103   宽城区 kcq kuanchengqu
100220104   朝阳区 cyq chaoyangqu
100220105   二道区 edq erdaoqu
100220106   绿园区 lyq lu:yuanqu
100220112   双阳区 syq shuangyangqu
100220113   九台区 jtq jiutaiqu
100220122   农安县 nax nonganxian
100220182   榆树市 yss yushushi
100220183   德惠市 dhs dehuishi
100220200   吉林市 jls jilinshi
100220201   市辖区 sxq shixiaqu
100220202   昌邑区 cyq changyiqu
100220203   龙潭区 ltq longtanqu
100220204   船营区 cyq chuanyingqu
100220211   丰满区 fmq fengmanqu
100220221   永吉县 yjx yongjixian
100220281   蛟河市 jhs jiaoheshi
100220282   桦甸市 hds huadianshi
100220283   舒兰市 sls shulanshi
100220284   磐石市 pss panshishi
100220300   四平市 sps sipingshi
100220301   市辖区 sxq shixiaqu
100220302   铁西区 txq tiexiqu
100220303   铁东区 tdq tiedongqu
100220322   梨树县 lsx lishuxian
100220323   伊通满族自治县 ytmzzzx yitongmanzuzizhixian
100220381   公主岭市    gzls    gongzhulingshi
100220382   双辽市 sls shuangliaoshi
100220400   辽源市 lys liaoyuanshi
100220401   市辖区 sxq shixiaqu
100220402   龙山区 lsq longshanqu
100220403   西安区 xaq xianqu
100220421   东丰县 dfx dongfengxian
100220422   东辽县 dlx dongliaoxian
100220500   通化市 ths tonghuashi
100220501   市辖区 sxq shixiaqu
100220502   东昌区 dcq dongchangqu
100220503   二道江区    edjq    erdaojiangqu
100220521   通化县 thx tonghuaxian
100220523   辉南县 hnx huinanxian
100220524   柳河县 lhx liuhexian
100220581   梅河口市    mhks    meihekoushi
100220582   集安市 jas jianshi
100220600   白山市 bss baishanshi
100220601   市辖区 sxq shixiaqu
100220602   浑江区 hjq hunjiangqu
100220605   江源区 jyq jiangyuanqu
100220621   抚松县 fsx fusongxian
100220622   靖宇县 jyx jingyuxian
100220623   长白朝鲜族自治县    zbcxzzzx    zhangbaichaoxianzuzizhixian
100220681   临江市 ljs linjiangshi
100220700   松原市 sys songyuanshi
100220701   市辖区 sxq shixiaqu
100220702   宁江区 njq ningjiangqu
100220721   前郭尔罗斯蒙古族自治县 qgelsmgzzzx qianguoerluosimengguzuzizhixian
100220722   长岭县 zlx zhanglingxian
100220723   乾安县 qax qiananxian
100220781   扶余市 fys fuyushi
100220800   白城市 bcs baichengshi
100220801   市辖区 sxq shixiaqu
100220802   洮北区 tbq taobeiqu
100220821   镇赉县 zlx zhenlaixian
100220822   通榆县 tyx tongyuxian
100220881   洮南市 tns taonanshi
100220882   大安市 das daanshi
100222400   延边朝鲜族自治州    ybcxzzzz    yanbianchaoxianzuzizhizhou
100222401   延吉市 yjs yanjishi
100222402   图们市 tms tumenshi
100222403   敦化市 dhs dunhuashi
100222404   珲春市 hcs hunchunshi
100222405   龙井市 ljs longjingshi
100222406   和龙市 hls helongshi
100222424   汪清县 wqx wangqingxian
100222426   安图县 atx antuxian
100230000   黑龙江省    hljs    heilongjiangsheng
100230100   哈尔滨市    hebs    haerbinshi
100230101   市辖区 sxq shixiaqu
100230102   道里区 dlq daoliqu
100230103   南岗区 ngq nangangqu
100230104   道外区 dwq daowaiqu
100230108   平房区 pfq pingfangqu
100230109   松北区 sbq songbeiqu
100230110   香坊区 xfq xiangfangqu
100230111   呼兰区 hlq hulanqu
100230112   阿城区 acq achengqu
100230123   依兰县 ylx yilanxian
100230124   方正县 fzx fangzhengxian
100230125   宾县  bx  binxian
100230126   巴彦县 byx bayanxian
100230127   木兰县 mlx mulanxian
100230128   通河县 thx tonghexian
100230129   延寿县 ysx yanshouxian
100230182   双城市 scs shuangchengshi
100230183   尚志市 szs shangzhishi
100230184   五常市 wcs wuchangshi
100230200   齐齐哈尔市   qqhes   qiqihaershi
100230201   市辖区 sxq shixiaqu
100230202   龙沙区 lsq longshaqu
100230203   建华区 jhq jianhuaqu
100230204   铁锋区 tfq tiefengqu
100230205   昂昂溪区    aaxq    angangxiqu
100230206   富拉尔基区   flejq   fulaerjiqu
100230207   碾子山区    nzsq    nianzishanqu
100230208   梅里斯达斡尔族区    mlsdwezq    meilisidawoerzuqu
100230221   龙江县 ljx longjiangxian
100230223   依安县 yax yianxian
100230224   泰来县 tlx tailaixian
100230225   甘南县 gnx gannanxian
100230227   富裕县 fyx fuyuxian
100230229   克山县 ksx keshanxian
100230230   克东县 kdx kedongxian
100230231   拜泉县 bqx baiquanxian
100230281   讷河市 nhs neheshi
100230300   鸡西市 jxs jixishi
100230301   市辖区 sxq shixiaqu
100230302   鸡冠区 jgq jiguanqu
100230303   恒山区 hsq hengshanqu
100230304   滴道区 ddq didaoqu
100230305   梨树区 lsq lishuqu
100230306   城子河区    czhq    chengzihequ
100230307   麻山区 msq mashanqu
100230321   鸡东县 jdx jidongxian
100230381   虎林市 hls hulinshi
100230382   密山市 mss mishanshi
100230400   鹤岗市 hgs hegangshi
100230401   市辖区 sxq shixiaqu
100230402   向阳区 xyq xiangyangqu
100230403   工农区 gnq gongnongqu
100230404   南山区 nsq nanshanqu
100230405   兴安区 xaq xinganqu
100230406   东山区 dsq dongshanqu
100230407   兴山区 xsq xingshanqu
100230421   萝北县 lbx luobeixian
100230422   绥滨县 sbx suibinxian
100230500   双鸭山市    syss    shuangyashanshi
100230501   市辖区 sxq shixiaqu
100230502   尖山区 jsq jianshanqu
100230503   岭东区 ldq lingdongqu
100230505   四方台区    sftq    sifangtaiqu
100230506   宝山区 bsq baoshanqu
100230521   集贤县 jxx jixianxian
100230522   友谊县 yyx youyixian
100230523   宝清县 bqx baoqingxian
100230524   饶河县 rhx raohexian
100230600   大庆市 dqs daqingshi
100230601   市辖区 sxq shixiaqu
100230602   萨尔图区    setq    saertuqu
100230603   龙凤区 lfq longfengqu
100230604   让胡路区    rhlq    ranghuluqu
100230605   红岗区 hgq honggangqu
100230606   大同区 dtq datongqu
100230621   肇州县 zzx zhaozhouxian
100230622   肇源县 zyx zhaoyuanxian
100230623   林甸县 ldx lindianxian
100230624   杜尔伯特蒙古族自治县  debtmgzzzx  duerbotemengguzuzizhixian
100230700   伊春市 ycs yichunshi
100230701   市辖区 sxq shixiaqu
100230702   伊春区 ycq yichunqu
100230703   南岔区 ncq nanchaqu
100230704   友好区 yhq youhaoqu
100230705   西林区 xlq xilinqu
100230706   翠峦区 clq cuiluanqu
100230707   新青区 xqq xinqingqu
100230708   美溪区 mxq meixiqu
100230709   金山屯区    jstq    jinshantunqu
100230710   五营区 wyq wuyingqu
100230711   乌马河区    wmhq    wumahequ
100230712   汤旺河区    twhq    tangwanghequ
100230713   带岭区 dlq dailingqu
100230714   乌伊岭区    wylq    wuyilingqu
100230715   红星区 hxq hongxingqu
100230716   上甘岭区    sglq    shangganlingqu
100230722   嘉荫县 jyx jiayinxian
100230781   铁力市 tls tielishi
100230800   佳木斯市    jmss    jiamusishi
100230801   市辖区 sxq shixiaqu
100230803   向阳区 xyq xiangyangqu
100230804   前进区 qjq qianjinqu
100230805   东风区 dfq dongfengqu
100230811   郊区  jq  jiaoqu
100230822   桦南县 hnx huananxian
100230826   桦川县 hcx huachuanxian
100230828   汤原县 tyx tangyuanxian
100230833   抚远县 fyx fuyuanxian
100230881   同江市 tjs tongjiangshi
100230882   富锦市 fjs fujinshi
100230900   七台河市    qths    qitaiheshi
100230901   市辖区 sxq shixiaqu
100230902   新兴区 xxq xinxingqu
100230903   桃山区 tsq taoshanqu
100230904   茄子河区    qzhq    qiezihequ
100230921   勃利县 blx bolixian
100231000   牡丹江市    mdjs    mudanjiangshi
100231001   市辖区 sxq shixiaqu
100231002   东安区 daq donganqu
100231003   阳明区 ymq yangmingqu
100231004   爱民区 amq aiminqu
100231005   西安区 xaq xianqu
100231024   东宁县 dnx dongningxian
100231025   林口县 lkx linkouxian
100231081   绥芬河市    sfhs    suifenheshi
100231083   海林市 hls hailinshi
100231084   宁安市 nas ninganshi
100231085   穆棱市 mls mulengshi
100231100   黑河市 hhs heiheshi
100231101   市辖区 sxq shixiaqu
100231102   爱辉区 ahq aihuiqu
100231121   嫩江县 njx nenjiangxian
100231123   逊克县 xkx xunkexian
100231124   孙吴县 swx sunwuxian
100231181   北安市 bas beianshi
100231182   五大连池市   wdlcs   wudalianchishi
100231200   绥化市 shs suihuashi
100231201   市辖区 sxq shixiaqu
100231202   北林区 blq beilinqu
100231221   望奎县 wkx wangkuixian
100231222   兰西县 lxx lanxixian
100231223   青冈县 qgx qinggangxian
100231224   庆安县 qax qinganxian
100231225   明水县 msx mingshuixian
100231226   绥棱县 slx suilengxian
100231281   安达市 ads andashi
100231282   肇东市 zds zhaodongshi
100231283   海伦市 hls hailunshi
100232700   大兴安岭地区  dxaldq  daxinganlingdiqu
100232721   呼玛县 hmx humaxian
100232722   塔河县 thx tahexian
100232723   漠河县 mhx mohexian
100310000   上海市 sh  shanghai
100310100   市辖区 sxq shixiaqu
100310101   黄浦区 hpq huangpuqu
100310104   徐汇区 xhq xuhuiqu
100310105   长宁区 znq zhangningqu
100310106   静安区 jaq jinganqu
100310107   普陀区 ptq putuoqu
100310108   闸北区 zbq zhabeiqu
100310109   虹口区 hkq hongkouqu
100310110   杨浦区 ypq yangpuqu
100310112   闵行区 mxq minxingqu
100310113   宝山区 bsq baoshanqu
100310114   嘉定区 jdq jiadingqu
100310115   浦东新区    pdxq    pudongxinqu
100310116   金山区 jsq jinshanqu
100310117   松江区 sjq songjiangqu
100310118   青浦区 qpq qingpuqu
100310120   奉贤区 fxq fengxianqu
100310200   县   x   xian
100310230   崇明县 cmx chongmingxian
100320000   江苏省 jss jiangsusheng
100320100   南京市 njs nanjingshi
100320101   市辖区 sxq shixiaqu
100320102   玄武区 xwq xuanwuqu
100320104   秦淮区 qhq qinhuaiqu
100320105   建邺区 jyq jianyequ
100320106   鼓楼区 glq gulouqu
100320111   浦口区 pkq pukouqu
100320113   栖霞区 qxq qixiaqu
100320114   雨花台区    yhtq    yuhuataiqu
100320115   江宁区 jnq jiangningqu
100320116   六合区 lhq liuhequ
100320117   溧水区 lsq lishuiqu
100320118   高淳区 gcq gaochunqu
100320200   无锡市 wxs wuxishi
100320201   市辖区 sxq shixiaqu
100320202   崇安区 caq chonganqu
100320203   南长区 nzq nanzhangqu
100320204   北塘区 btq beitangqu
100320205   锡山区 xsq xishanqu
100320206   惠山区 hsq huishanqu
100320211   滨湖区 bhq binhuqu
100320281   江阴市 jys jiangyinshi
100320282   宜兴市 yxs yixingshi
100320300   徐州市 xzs xuzhoushi
100320301   市辖区 sxq shixiaqu
100320302   鼓楼区 glq gulouqu
100320303   云龙区 ylq yunlongqu
100320305   贾汪区 jwq jiawangqu
100320311   泉山区 qsq quanshanqu
100320312   铜山区 tsq tongshanqu
100320321   丰县  fx  fengxian
100320322   沛县  px  peixian
100320324   睢宁县 snx suiningxian
100320381   新沂市 xys xinyishi
100320382   邳州市 pzs pizhoushi
100320400   常州市 czs changzhoushi
100320401   市辖区 sxq shixiaqu
100320402   天宁区 tnq tianningqu
100320404   钟楼区 zlq zhonglouqu
100320405   戚墅堰区    qsyq    qishuyanqu
100320411   新北区 xbq xinbeiqu
100320412   武进区 wjq wujinqu
100320481   溧阳市 lys liyangshi
100320482   金坛市 jts jintanshi
100320500   苏州市 szs suzhoushi
100320501   市辖区 sxq shixiaqu
100320505   虎丘区 hqq huqiuqu
100320506   吴中区 wzq wuzhongqu
100320507   相城区 xcq xiangchengqu
100320508   姑苏区 gsq gusuqu
100320509   吴江区 wjq wujiangqu
100320581   常熟市 css changshushi
100320582   张家港市    zjgs    zhangjiagangshi
100320583   昆山市 kss kunshanshi
100320585   太仓市 tcs taicangshi
100320600   南通市 nts nantongshi
100320601   市辖区 sxq shixiaqu
100320602   崇川区 ccq chongchuanqu
100320611   港闸区 gzq gangzhaqu
100320612   通州区 tzq tongzhouqu
100320621   海安县 hax haianxian
100320623   如东县 rdx rudongxian
100320681   启东市 qds qidongshi
100320682   如皋市 rgs rugaoshi
100320684   海门市 hms haimenshi
100320700   连云港市    lygs    lianyungangshi
100320701   市辖区 sxq shixiaqu
100320703   连云区 lyq lianyunqu
100320706   海州区 hzq haizhouqu
100320707   赣榆区 gyq ganyuqu
100320722   东海县 dhx donghaixian
100320723   灌云县 gyx guanyunxian
100320724   灌南县 gnx guannanxian
100320800   淮安市 has huaianshi
100320801   市辖区 sxq shixiaqu
100320802   清河区 qhq qinghequ
100320803   淮安区 haq huaianqu
100320804   淮阴区 hyq huaiyinqu
100320811   清浦区 qpq qingpuqu
100320826   涟水县 lsx lianshuixian
100320829   洪泽县 hzx hongzexian
100320830   盱眙县 xyx xuyixian
100320831   金湖县 jhx jinhuxian
100320900   盐城市 ycs yanchengshi
100320901   市辖区 sxq shixiaqu
100320902   亭湖区 thq tinghuqu
100320903   盐都区 ydq yandouqu
100320921   响水县 xsx xiangshuixian
100320922   滨海县 bhx binhaixian
100320923   阜宁县 fnx funingxian
100320924   射阳县 syx sheyangxian
100320925   建湖县 jhx jianhuxian
100320981   东台市 dts dongtaishi
100320982   大丰市 dfs dafengshi
100321000   扬州市 yzs yangzhoushi
100321001   市辖区 sxq shixiaqu
100321002   广陵区 glq guanglingqu
100321003   邗江区 hjq hanjiangqu
100321012   江都区 jdq jiangdouqu
100321023   宝应县 byx baoyingxian
100321081   仪征市 yzs yizhengshi
100321084   高邮市 gys gaoyoushi
100321100   镇江市 zjs zhenjiangshi
100321101   市辖区 sxq shixiaqu
100321102   京口区 jkq jingkouqu
100321111   润州区 rzq runzhouqu
100321112   丹徒区 dtq dantuqu
100321181   丹阳市 dys danyangshi
100321182   扬中市 yzs yangzhongshi
100321183   句容市 jrs jurongshi
100321200   泰州市 tzs taizhoushi
100321201   市辖区 sxq shixiaqu
100321202   海陵区 hlq hailingqu
100321203   高港区 ggq gaogangqu
100321204   姜堰区 jyq jiangyanqu
100321281   兴化市 xhs xinghuashi
100321282   靖江市 jjs jingjiangshi
100321283   泰兴市 txs taixingshi
100321300   宿迁市 sqs suqianshi
100321301   市辖区 sxq shixiaqu
100321302   宿城区 scq suchengqu
100321311   宿豫区 syq suyuqu
100321322   沭阳县 syx shuyangxian
100321323   泗阳县 syx siyangxian
100321324   泗洪县 shx sihongxian
100330000   浙江省 zjs zhejiangsheng
100330100   杭州市 hzs hangzhoushi
100330101   市辖区 sxq shixiaqu
100330102   上城区 scq shangchengqu
100330103   下城区 xcq xiachengqu
100330104   江干区 jgq jiangganqu
100330105   拱墅区 gsq gongshuqu
100330106   西湖区 xhq xihuqu
100330108   滨江区 bjq binjiangqu
100330109   萧山区 xsq xiaoshanqu
100330110   余杭区 yhq yuhangqu
100330122   桐庐县 tlx tongluxian
100330127   淳安县 cax chunanxian
100330182   建德市 jds jiandeshi
100330183   富阳市 fys fuyangshi
100330185   临安市 las linanshi
100330200   宁波市 nbs ningboshi
100330201   市辖区 sxq shixiaqu
100330203   海曙区 hsq haishuqu
100330204   江东区 jdq jiangdongqu
100330205   江北区 jbq jiangbeiqu
100330206   北仑区 blq beilunqu
100330211   镇海区 zhq zhenhaiqu
100330212   鄞州区 yzq yinzhouqu
100330225   象山县 xsx xiangshanxian
100330226   宁海县 nhx ninghaixian
100330281   余姚市 yys yuyaoshi
100330282   慈溪市 cxs cixishi
100330283   奉化市 fhs fenghuashi
100330300   温州市 wzs wenzhoushi
100330301   市辖区 sxq shixiaqu
100330302   鹿城区 lcq luchengqu
100330303   龙湾区 lwq longwanqu
100330304   瓯海区 ohq ouhaiqu
100330322   洞头县 dtx dongtouxian
100330324   永嘉县 yjx yongjiaxian
100330326   平阳县 pyx pingyangxian
100330327   苍南县 cnx cangnanxian
100330328   文成县 wcx wenchengxian
100330329   泰顺县 tsx taishunxian
100330381   瑞安市 ras ruianshi
100330382   乐清市 lqs leqingshi
100330400   嘉兴市 jxs jiaxingshi
100330401   市辖区 sxq shixiaqu
100330402   南湖区 nhq nanhuqu
100330411   秀洲区 xzq xiuzhouqu
100330421   嘉善县 jsx jiashanxian
100330424   海盐县 hyx haiyanxian
100330481   海宁市 hns hainingshi
100330482   平湖市 phs pinghushi
100330483   桐乡市 txs tongxiangshi
100330500   湖州市 hzs huzhoushi
100330501   市辖区 sxq shixiaqu
100330502   吴兴区 wxq wuxingqu
100330503   南浔区 nxq nanxunqu
100330521   德清县 dqx deqingxian
100330522   长兴县 zxx zhangxingxian
100330523   安吉县 ajx anjixian
100330600   绍兴市 sxs shaoxingshi
100330601   市辖区 sxq shixiaqu
100330602   越城区 ycq yuechengqu
100330603   柯桥区 kqq keqiaoqu
100330604   上虞区 syq shangyuqu
100330624   新昌县 xcx xinchangxian
100330681   诸暨市 zjs zhujishi
100330683   嵊州市 szs shengzhoushi
100330700   金华市 jhs jinhuashi
100330701   市辖区 sxq shixiaqu
100330702   婺城区 wcq wuchengqu
100330703   金东区 jdq jindongqu
100330723   武义县 wyx wuyixian
100330726   浦江县 pjx pujiangxian
100330727   磐安县 pax pananxian
100330781   兰溪市 lxs lanxishi
100330782   义乌市 yws yiwushi
100330783   东阳市 dys dongyangshi
100330784   永康市 yks yongkangshi
100330800   衢州市 qzs quzhoushi
100330801   市辖区 sxq shixiaqu
100330802   柯城区 kcq kechengqu
100330803   衢江区 qjq qujiangqu
100330822   常山县 csx changshanxian
100330824   开化县 khx kaihuaxian
100330825   龙游县 lyx longyouxian
100330881   江山市 jss jiangshanshi
100330900   舟山市 zss zhoushanshi
100330901   市辖区 sxq shixiaqu
100330902   定海区 dhq dinghaiqu
100330903   普陀区 ptq putuoqu
100330921   岱山县 dsx daishanxian
100330922   嵊泗县 ssx shengsixian
100331000   台州市 tzs taizhoushi
100331001   市辖区 sxq shixiaqu
100331002   椒江区 jjq jiaojiangqu
100331003   黄岩区 hyq huangyanqu
100331004   路桥区 lqq luqiaoqu
100331021   玉环县 yhx yuhuanxian
100331022   三门县 smx sanmenxian
100331023   天台县 ttx tiantaixian
100331024   仙居县 xjx xianjuxian
100331081   温岭市 wls wenlingshi
100331082   临海市 lhs linhaishi
100331100   丽水市 lss lishuishi
100331101   市辖区 sxq shixiaqu
100331102   莲都区 ldq liandouqu
100331121   青田县 qtx qingtianxian
100331122   缙云县 jyx jinyunxian
100331123   遂昌县 scx suichangxian
100331124   松阳县 syx songyangxian
100331125   云和县 yhx yunhexian
100331126   庆元县 qyx qingyuanxian
100331127   景宁畲族自治县 jnszzzx jingningshezuzizhixian
100331181   龙泉市 lqs longquanshi
100340000   安徽省 ahs anhuisheng
100340100   合肥市 hfs hefeishi
100340101   市辖区 sxq shixiaqu
100340102   瑶海区 yhq yaohaiqu
100340103   庐阳区 lyq luyangqu
100340104   蜀山区 ssq shushanqu
100340111   包河区 bhq baohequ
100340121   长丰县 zfx zhangfengxian
100340122   肥东县 fdx feidongxian
100340123   肥西县 fxx feixixian
100340124   庐江县 ljx lujiangxian
100340181   巢湖市 chs chaohushi
100340200   芜湖市 whs wuhushi
100340201   市辖区 sxq shixiaqu
100340202   镜湖区 jhq jinghuqu
100340203   弋江区 yjq yijiangqu
100340207   鸠江区 jjq jiujiangqu
100340208   三山区 ssq sanshanqu
100340221   芜湖县 whx wuhuxian
100340222   繁昌县 fcx fanchangxian
100340223   南陵县 nlx nanlingxian
100340225   无为县 wwx wuweixian
100340300   蚌埠市 bbs bangbushi
100340301   市辖区 sxq shixiaqu
100340302   龙子湖区    lzhq    longzihuqu
100340303   蚌山区 bsq bangshanqu
100340304   禹会区 yhq yuhuiqu
100340311   淮上区 hsq huaishangqu
100340321   怀远县 hyx huaiyuanxian
100340322   五河县 whx wuhexian
100340323   固镇县 gzx guzhenxian
100340400   淮南市 hns huainanshi
100340401   市辖区 sxq shixiaqu
100340402   大通区 dtq datongqu
100340403   田家庵区    tjaq    tianjiaanqu
100340404   谢家集区    xjjq    xiejiajiqu
100340405   八公山区    bgsq    bagongshanqu
100340406   潘集区 pjq panjiqu
100340421   凤台县 ftx fengtaixian
100340500   马鞍山市    mass    maanshanshi
100340501   市辖区 sxq shixiaqu
100340503   花山区 hsq huashanqu
100340504   雨山区 ysq yushanqu
100340506   博望区 bwq bowangqu
100340521   当涂县 dtx dangtuxian
100340522   含山县 hsx hanshanxian
100340523   和县  hx  hexian
100340600   淮北市 hbs huaibeishi
100340601   市辖区 sxq shixiaqu
100340602   杜集区 djq dujiqu
100340603   相山区 xsq xiangshanqu
100340604   烈山区 lsq lieshanqu
100340621   濉溪县 sxx suixixian
100340700   铜陵市 tls tonglingshi
100340701   市辖区 sxq shixiaqu
100340702   铜官山区    tgsq    tongguanshanqu
100340703   狮子山区    szsq    shizishanqu
100340711   郊区  jq  jiaoqu
100340721   铜陵县 tlx tonglingxian
100340800   安庆市 aqs anqingshi
100340801   市辖区 sxq shixiaqu
100340802   迎江区 yjq yingjiangqu
100340803   大观区 dgq daguanqu
100340811   宜秀区 yxq yixiuqu
100340822   怀宁县 hnx huainingxian
100340823   枞阳县 zyx zongyangxian
100340824   潜山县 qsx qianshanxian
100340825   太湖县 thx taihuxian
100340826   宿松县 ssx susongxian
100340827   望江县 wjx wangjiangxian
100340828   岳西县 yxx yuexixian
100340881   桐城市 tcs tongchengshi
100341000   黄山市 hss huangshanshi
100341001   市辖区 sxq shixiaqu
100341002   屯溪区 txq tunxiqu
100341003   黄山区 hsq huangshanqu
100341004   徽州区 hzq huizhouqu
100341021   歙县  sx  shexian
100341022   休宁县 xnx xiuningxian
100341023   黟县  yx  yixian
100341024   祁门县 qmx qimenxian
100341100   滁州市 czs chuzhoushi
100341101   市辖区 sxq shixiaqu
100341102   琅琊区 lyq langyaqu
100341103   南谯区 nqq nanqiaoqu
100341122   来安县 lax laianxian
100341124   全椒县 qjx quanjiaoxian
100341125   定远县 dyx dingyuanxian
100341126   凤阳县 fyx fengyangxian
100341181   天长市 tzs tianzhangshi
100341182   明光市 mgs mingguangshi
100341200   阜阳市 fys fuyangshi
100341201   市辖区 sxq shixiaqu
100341202   颍州区 yzq yingzhouqu
100341203   颍东区 ydq yingdongqu
100341204   颍泉区 yqq yingquanqu
100341221   临泉县 lqx linquanxian
100341222   太和县 thx taihexian
100341225   阜南县 fnx funanxian
100341226   颍上县 ysx yingshangxian
100341282   界首市 jss jieshoushi
100341300   宿州市 szs suzhoushi
100341301   市辖区 sxq shixiaqu
100341302   埇桥区 yqq yongqiaoqu
100341321   砀山县 dsx dangshanxian
100341322   萧县  xx  xiaoxian
100341323   灵璧县 lbx lingbixian
100341324   泗县  sx  sixian
100341500   六安市 las liuanshi
100341501   市辖区 sxq shixiaqu
100341502   金安区 jaq jinanqu
100341503   裕安区 yaq yuanqu
100341521   寿县  sx  shouxian
100341522   霍邱县 hqx huoqiuxian
100341523   舒城县 scx shuchengxian
100341524   金寨县 jzx jinzhaixian
100341525   霍山县 hsx huoshanxian
100341600   亳州市 bzs bozhoushi
100341601   市辖区 sxq shixiaqu
100341602   谯城区 qcq qiaochengqu
100341621   涡阳县 wyx woyangxian
100341622   蒙城县 mcx mengchengxian
100341623   利辛县 lxx lixinxian
100341700   池州市 czs chizhoushi
100341701   市辖区 sxq shixiaqu
100341702   贵池区 gcq guichiqu
100341721   东至县 dzx dongzhixian
100341722   石台县 stx shitaixian
100341723   青阳县 qyx qingyangxian
100341800   宣城市 xcs xuanchengshi
100341801   市辖区 sxq shixiaqu
100341802   宣州区 xzq xuanzhouqu
100341821   郎溪县 lxx langxixian
100341822   广德县 gdx guangdexian
100341823   泾县  jx  jingxian
100341824   绩溪县 jxx jixixian
100341825   旌德县 jdx jingdexian
100341881   宁国市 ngs ningguoshi
100350000   福建省 fjs fujiansheng
100350100   福州市 fzs fuzhoushi
100350101   市辖区 sxq shixiaqu
100350102   鼓楼区 glq gulouqu
100350103   台江区 tjq taijiangqu
100350104   仓山区 csq cangshanqu
100350105   马尾区 mwq maweiqu
100350111   晋安区 jaq jinanqu
100350121   闽侯县 mhx minhouxian
100350122   连江县 ljx lianjiangxian
100350123   罗源县 lyx luoyuanxian
100350124   闽清县 mqx minqingxian
100350125   永泰县 ytx yongtaixian
100350128   平潭县 ptx pingtanxian
100350181   福清市 fqs fuqingshi
100350182   长乐市 zls zhangleshi
100350200   厦门市 sms shamenshi
100350201   市辖区 sxq shixiaqu
100350203   思明区 smq simingqu
100350205   海沧区 hcq haicangqu
100350206   湖里区 hlq huliqu
100350211   集美区 jmq jimeiqu
100350212   同安区 taq tonganqu
100350213   翔安区 xaq xianganqu
100350300   莆田市 pts putianshi
100350301   市辖区 sxq shixiaqu
100350302   城厢区 cxq chengxiangqu
100350303   涵江区 hjq hanjiangqu
100350304   荔城区 lcq lichengqu
100350305   秀屿区 xyq xiuyuqu
100350322   仙游县 xyx xianyouxian
100350400   三明市 sms sanmingshi
100350401   市辖区 sxq shixiaqu
100350402   梅列区 mlq meiliequ
100350403   三元区 syq sanyuanqu
100350421   明溪县 mxx mingxixian
100350423   清流县 qlx qingliuxian
100350424   宁化县 nhx ninghuaxian
100350425   大田县 dtx datianxian
100350426   尤溪县 yxx youxixian
100350427   沙县  sx  shaxian
100350428   将乐县 jlx jianglexian
100350429   泰宁县 tnx tainingxian
100350430   建宁县 jnx jianningxian
100350481   永安市 yas yonganshi
100350500   泉州市 qzs quanzhoushi
100350501   市辖区 sxq shixiaqu
100350502   鲤城区 lcq lichengqu
100350503   丰泽区 fzq fengzequ
100350504   洛江区 ljq luojiangqu
100350505   泉港区 qgq quangangqu
100350521   惠安县 hax huianxian
100350524   安溪县 axx anxixian
100350525   永春县 ycx yongchunxian
100350526   德化县 dhx dehuaxian
100350527   金门县 jmx jinmenxian
100350581   石狮市 sss shishishi
100350582   晋江市 jjs jinjiangshi
100350583   南安市 nas nananshi
100350600   漳州市 zzs zhangzhoushi
100350601   市辖区 sxq shixiaqu
100350602   芗城区 xcq xiangchengqu
100350603   龙文区 lwq longwenqu
100350622   云霄县 yxx yunxiaoxian
100350623   漳浦县 zpx zhangpuxian
100350624   诏安县 zax zhaoanxian
100350625   长泰县 ztx zhangtaixian
100350626   东山县 dsx dongshanxian
100350627   南靖县 njx nanjingxian
100350628   平和县 phx pinghexian
100350629   华安县 hax huaanxian
100350681   龙海市 lhs longhaishi
100350700   南平市 nps nanpingshi
100350701   市辖区 sxq shixiaqu
100350702   延平区 ypq yanpingqu
100350721   顺昌县 scx shunchangxian
100350722   浦城县 pcx puchengxian
100350723   光泽县 gzx guangzexian
100350724   松溪县 sxx songxixian
100350725   政和县 zhx zhenghexian
100350781   邵武市 sws shaowushi
100350782   武夷山市    wyss    wuyishanshi
100350783   建瓯市 jos jianoushi
100350784   建阳市 jys jianyangshi
100350800   龙岩市 lys longyanshi
100350801   市辖区 sxq shixiaqu
100350802   新罗区 xlq xinluoqu
100350821   长汀县 ztx zhangtingxian
100350822   永定县 ydx yongdingxian
100350823   上杭县 shx shanghangxian
100350824   武平县 wpx wupingxian
100350825   连城县 lcx lianchengxian
100350881   漳平市 zps zhangpingshi
100350900   宁德市 nds ningdeshi
100350901   市辖区 sxq shixiaqu
100350902   蕉城区 jcq jiaochengqu
100350921   霞浦县 xpx xiapuxian
100350922   古田县 gtx gutianxian
100350923   屏南县 pnx pingnanxian
100350924   寿宁县 snx shouningxian
100350925   周宁县 znx zhouningxian
100350926   柘荣县 zrx zherongxian
100350981   福安市 fas fuanshi
100350982   福鼎市 fds fudingshi
100360000   江西省 jxs jiangxisheng
100360100   南昌市 ncs nanchangshi
100360101   市辖区 sxq shixiaqu
100360102   东湖区 dhq donghuqu
100360103   西湖区 xhq xihuqu
100360104   青云谱区    qypq    qingyunpuqu
100360105   湾里区 wlq wanliqu
100360111   青山湖区    qshq    qingshanhuqu
100360121   南昌县 ncx nanchangxian
100360122   新建县 xjx xinjianxian
100360123   安义县 ayx anyixian
100360124   进贤县 jxx jinxianxian
100360200   景德镇市    jdzs    jingdezhenshi
100360201   市辖区 sxq shixiaqu
100360202   昌江区 cjq changjiangqu
100360203   珠山区 zsq zhushanqu
100360222   浮梁县 flx fuliangxian
100360281   乐平市 lps lepingshi
100360300   萍乡市 pxs pingxiangshi
100360301   市辖区 sxq shixiaqu
100360302   安源区 ayq anyuanqu
100360313   湘东区 xdq xiangdongqu
100360321   莲花县 lhx lianhuaxian
100360322   上栗县 slx shanglixian
100360323   芦溪县 lxx luxixian
100360400   九江市 jjs jiujiangshi
100360401   市辖区 sxq shixiaqu
100360402   庐山区 lsq lushanqu
100360403   浔阳区 xyq xunyangqu
100360421   九江县 jjx jiujiangxian
100360423   武宁县 wnx wuningxian
100360424   修水县 xsx xiushuixian
100360425   永修县 yxx yongxiuxian
100360426   德安县 dax deanxian
100360427   星子县 xzx xingzixian
100360428   都昌县 dcx douchangxian
100360429   湖口县 hkx hukouxian
100360430   彭泽县 pzx pengzexian
100360481   瑞昌市 rcs ruichangshi
100360482   共青城市    gqcs    gongqingchengshi
100360500   新余市 xys xinyushi
100360501   市辖区 sxq shixiaqu
100360502   渝水区 ysq yushuiqu
100360521   分宜县 fyx fenyixian
100360600   鹰潭市 yts yingtanshi
100360601   市辖区 sxq shixiaqu
100360602   月湖区 yhq yuehuqu
100360622   余江县 yjx yujiangxian
100360681   贵溪市 gxs guixishi
100360700   赣州市 gzs ganzhoushi
100360701   市辖区 sxq shixiaqu
100360702   章贡区 zgq zhanggongqu
100360703   南康区 nkq nankangqu
100360721   赣县  gx  ganxian
100360722   信丰县 xfx xinfengxian
100360723   大余县 dyx dayuxian
100360724   上犹县 syx shangyouxian
100360725   崇义县 cyx chongyixian
100360726   安远县 ayx anyuanxian
100360727   龙南县 lnx longnanxian
100360728   定南县 dnx dingnanxian
100360729   全南县 qnx quannanxian
100360730   宁都县 ndx ningdouxian
100360731   于都县 ydx yudouxian
100360732   兴国县 xgx xingguoxian
100360733   会昌县 hcx huichangxian
100360734   寻乌县 xwx xunwuxian
100360735   石城县 scx shichengxian
100360781   瑞金市 rjs ruijinshi
100360800   吉安市 jas jianshi
100360801   市辖区 sxq shixiaqu
100360802   吉州区 jzq jizhouqu
100360803   青原区 qyq qingyuanqu
100360821   吉安县 jax jianxian
100360822   吉水县 jsx jishuixian
100360823   峡江县 xjx xiajiangxian
100360824   新干县 xgx xinganxian
100360825   永丰县 yfx yongfengxian
100360826   泰和县 thx taihexian
100360827   遂川县 scx suichuanxian
100360828   万安县 wax wananxian
100360829   安福县 afx anfuxian
100360830   永新县 yxx yongxinxian
100360881   井冈山市    jgss    jinggangshanshi
100360900   宜春市 ycs yichunshi
100360901   市辖区 sxq shixiaqu
100360902   袁州区 yzq yuanzhouqu
100360921   奉新县 fxx fengxinxian
100360922   万载县 wzx wanzaixian
100360923   上高县 sgx shanggaoxian
100360924   宜丰县 yfx yifengxian
100360925   靖安县 jax jinganxian
100360926   铜鼓县 tgx tongguxian
100360981   丰城市 fcs fengchengshi
100360982   樟树市 zss zhangshushi
100360983   高安市 gas gaoanshi
100361000   抚州市 fzs fuzhoushi
100361001   市辖区 sxq shixiaqu
100361002   临川区 lcq linchuanqu
100361021   南城县 ncx nanchengxian
100361022   黎川县 lcx lichuanxian
100361023   南丰县 nfx nanfengxian
100361024   崇仁县 crx chongrenxian
100361025   乐安县 lax leanxian
100361026   宜黄县 yhx yihuangxian
100361027   金溪县 jxx jinxixian
100361028   资溪县 zxx zixixian
100361029   东乡县 dxx dongxiangxian
100361030   广昌县 gcx guangchangxian
100361100   上饶市 srs shangraoshi
100361101   市辖区 sxq shixiaqu
100361102   信州区 xzq xinzhouqu
100361121   上饶县 srx shangraoxian
100361122   广丰县 gfx guangfengxian
100361123   玉山县 ysx yushanxian
100361124   铅山县 qsx qianshanxian
100361125   横峰县 hfx hengfengxian
100361126   弋阳县 yyx yiyangxian
100361127   余干县 ygx yuganxian
100361128   鄱阳县 pyx poyangxian
100361129   万年县 wnx wannianxian
100361130   婺源县 wyx wuyuanxian
100361181   德兴市 dxs dexingshi
100370000   山东省 sds shandongsheng
100370100   济南市 jns jinanshi
100370101   市辖区 sxq shixiaqu
100370102   历下区 lxq lixiaqu
100370103   市中区 szq shizhongqu
100370104   槐荫区 hyq huaiyinqu
100370105   天桥区 tqq tianqiaoqu
100370112   历城区 lcq lichengqu
100370113   长清区 zqq zhangqingqu
100370124   平阴县 pyx pingyinxian
100370125   济阳县 jyx jiyangxian
100370126   商河县 shx shanghexian
100370181   章丘市 zqs zhangqiushi
100370200   青岛市 qds qingdaoshi
100370201   市辖区 sxq shixiaqu
100370202   市南区 snq shinanqu
100370203   市北区 sbq shibeiqu
100370211   黄岛区 hdq huangdaoqu
100370212   崂山区 lsq laoshanqu
100370213   李沧区 lcq licangqu
100370214   城阳区 cyq chengyangqu
100370281   胶州市 jzs jiaozhoushi
100370282   即墨市 jms jimoshi
100370283   平度市 pds pingdushi
100370285   莱西市 lxs laixishi
100370300   淄博市 zbs ziboshi
100370301   市辖区 sxq shixiaqu
100370302   淄川区 zcq zichuanqu
100370303   张店区 zdq zhangdianqu
100370304   博山区 bsq boshanqu
100370305   临淄区 lzq linziqu
100370306   周村区 zcq zhoucunqu
100370321   桓台县 htx huantaixian
100370322   高青县 gqx gaoqingxian
100370323   沂源县 yyx yiyuanxian
100370400   枣庄市 zzs zaozhuangshi
100370401   市辖区 sxq shixiaqu
100370402   市中区 szq shizhongqu
100370403   薛城区 xcq xuechengqu
100370404   峄城区 ycq yichengqu
100370405   台儿庄区    tezq    taierzhuangqu
100370406   山亭区 stq shantingqu
100370481   滕州市 tzs tengzhoushi
100370500   东营市 dys dongyingshi
100370501   市辖区 sxq shixiaqu
100370502   东营区 dyq dongyingqu
100370503   河口区 hkq hekouqu
100370521   垦利县 klx kenlixian
100370522   利津县 ljx lijinxian
100370523   广饶县 grx guangraoxian
100370600   烟台市 yts yantaishi
100370601   市辖区 sxq shixiaqu
100370602   芝罘区 zfq zhifuqu
100370611   福山区 fsq fushanqu
100370612   牟平区 mpq moupingqu
100370613   莱山区 lsq laishanqu
100370634   长岛县 zdx zhangdaoxian
100370681   龙口市 lks longkoushi
100370682   莱阳市 lys laiyangshi
100370683   莱州市 lzs laizhoushi
100370684   蓬莱市 pls penglaishi
100370685   招远市 zys zhaoyuanshi
100370686   栖霞市 qxs qixiashi
100370687   海阳市 hys haiyangshi
100370700   潍坊市 wfs weifangshi
100370701   市辖区 sxq shixiaqu
100370702   潍城区 wcq weichengqu
100370703   寒亭区 htq hantingqu
100370704   坊子区 fzq fangziqu
100370705   奎文区 kwq kuiwenqu
100370724   临朐县 lqx linquxian
100370725   昌乐县 clx changlexian
100370781   青州市 qzs qingzhoushi
100370782   诸城市 zcs zhuchengshi
100370783   寿光市 sgs shouguangshi
100370784   安丘市 aqs anqiushi
100370785   高密市 gms gaomishi
100370786   昌邑市 cys changyishi
100370800   济宁市 jns jiningshi
100370801   市辖区 sxq shixiaqu
100370811   任城区 rcq renchengqu
100370812   兖州区 yzq yanzhouqu
100370826   微山县 wsx weishanxian
100370827   鱼台县 ytx yutaixian
100370828   金乡县 jxx jinxiangxian
100370829   嘉祥县 jxx jiaxiangxian
100370830   汶上县 wsx wenshangxian
100370831   泗水县 ssx sishuixian
100370832   梁山县 lsx liangshanxian
100370881   曲阜市 qfs qufushi
100370883   邹城市 zcs zouchengshi
100370900   泰安市 tas taianshi
100370901   市辖区 sxq shixiaqu
100370902   泰山区 tsq taishanqu
100370911   岱岳区 dyq daiyuequ
100370921   宁阳县 nyx ningyangxian
100370923   东平县 dpx dongpingxian
100370982   新泰市 xts xintaishi
100370983   肥城市 fcs feichengshi
100371000   威海市 whs weihaishi
100371001   市辖区 sxq shixiaqu
100371002   环翠区 hcq huancuiqu
100371003   文登区 wdq wendengqu
100371082   荣成市 rcs rongchengshi
100371083   乳山市 rss rushanshi
100371100   日照市 rzs rizhaoshi
100371101   市辖区 sxq shixiaqu
100371102   东港区 dgq donggangqu
100371103   岚山区 lsq lanshanqu
100371121   五莲县 wlx wulianxian
100371122   莒县  jx  juxian
100371200   莱芜市 lws laiwushi
100371201   市辖区 sxq shixiaqu
100371202   莱城区 lcq laichengqu
100371203   钢城区 gcq gangchengqu
100371300   临沂市 lys linyishi
100371301   市辖区 sxq shixiaqu
100371302   兰山区 lsq lanshanqu
100371311   罗庄区 lzq luozhuangqu
100371312   河东区 hdq hedongqu
100371321   沂南县 ynx yinanxian
100371322   郯城县 tcx tanchengxian
100371323   沂水县 ysx yishuixian
100371324   兰陵县 llx lanlingxian
100371325   费县  fx  feixian
100371326   平邑县 pyx pingyixian
100371327   莒南县 jnx junanxian
100371328   蒙阴县 myx mengyinxian
100371329   临沭县 lsx linshuxian
100371400   德州市 dzs dezhoushi
100371401   市辖区 sxq shixiaqu
100371402   德城区 dcq dechengqu
100371403   陵城区 lcq lingchengqu
100371422   宁津县 njx ningjinxian
100371423   庆云县 qyx qingyunxian
100371424   临邑县 lyx linyixian
100371425   齐河县 qhx qihexian
100371426   平原县 pyx pingyuanxian
100371427   夏津县 xjx xiajinxian
100371428   武城县 wcx wuchengxian
100371481   乐陵市 lls lelingshi
100371482   禹城市 ycs yuchengshi
100371500   聊城市 lcs liaochengshi
100371501   市辖区 sxq shixiaqu
100371502   东昌府区    dcfq    dongchangfuqu
100371521   阳谷县 ygx yangguxian
100371522   莘县  xx  xinxian
100371523   茌平县 cpx chipingxian
100371524   东阿县 dax dongaxian
100371525   冠县  gx  guanxian
100371526   高唐县 gtx gaotangxian
100371581   临清市 lqs linqingshi
100371600   滨州市 bzs binzhoushi
100371601   市辖区 sxq shixiaqu
100371602   滨城区 bcq binchengqu
100371603   沾化区 zhq zhanhuaqu
100371621   惠民县 hmx huiminxian
100371622   阳信县 yxx yangxinxian
100371623   无棣县 wdx wudixian
100371625   博兴县 bxx boxingxian
100371626   邹平县 zpx zoupingxian
100371700   菏泽市 hzs hezeshi
100371701   市辖区 sxq shixiaqu
100371702   牡丹区 mdq mudanqu
100371721   曹县  cx  caoxian
100371722   单县  dx  danxian
100371723   成武县 cwx chengwuxian
100371724   巨野县 jyx juyexian
100371725   郓城县 ycx yunchengxian
100371726   鄄城县 jcx juanchengxian
100371727   定陶县 dtx dingtaoxian
100371728   东明县 dmx dongmingxian
100410000   河南省 hns henansheng
100410100   郑州市 zzs zhengzhoushi
100410101   市辖区 sxq shixiaqu
100410102   中原区 zyq zhongyuanqu
100410103   二七区 eqq erqiqu
100410104   管城回族区   gchzq   guanchenghuizuqu
100410105   金水区 jsq jinshuiqu
100410106   上街区 sjq shangjiequ
100410108   惠济区 hjq huijiqu
100410122   中牟县 zmx zhongmouxian
100410181   巩义市 gys gongyishi
100410182   荥阳市 yys yingyangshi
100410183   新密市 xms xinmishi
100410184   新郑市 xzs xinzhengshi
100410185   登封市 dfs dengfengshi
100410200   开封市 kfs kaifengshi
100410201   市辖区 sxq shixiaqu
100410202   龙亭区 ltq longtingqu
100410203   顺河回族区   shhzq   shunhehuizuqu
100410204   鼓楼区 glq gulouqu
100410205   禹王台区    ywtq    yuwangtaiqu
100410211   金明区 jmq jinmingqu
100410221   杞县  qx  qixian
100410222   通许县 txx tongxuxian
100410223   尉氏县 wsx weishixian
100410224   开封县 kfx kaifengxian
100410225   兰考县 lkx lankaoxian
100410300   洛阳市 lys luoyangshi
100410301   市辖区 sxq shixiaqu
100410302   老城区 lcq laochengqu
100410303   西工区 xgq xigongqu
100410304   瀍河回族区   chhzq   chanhehuizuqu
100410305   涧西区 jxq jianxiqu
100410306   吉利区 jlq jiliqu
100410311   洛龙区 llq luolongqu
100410322   孟津县 mjx mengjinxian
100410323   新安县 xax xinanxian
100410324   栾川县 lcx luanchuanxian
100410325   嵩县  sx  songxian
100410326   汝阳县 ryx ruyangxian
100410327   宜阳县 yyx yiyangxian
100410328   洛宁县 lnx luoningxian
100410329   伊川县 ycx yichuanxian
100410381   偃师市 yss yanshishi
100410400   平顶山市    pdss    pingdingshanshi
100410401   市辖区 sxq shixiaqu
100410402   新华区 xhq xinhuaqu
100410403   卫东区 wdq weidongqu
100410404   石龙区 slq shilongqu
100410411   湛河区 zhq zhanhequ
100410421   宝丰县 bfx baofengxian
100410422   叶县  yx  yexian
100410423   鲁山县 lsx lushanxian
100410425   郏县  jx  jiaxian
100410481   舞钢市 wgs wugangshi
100410482   汝州市 rzs ruzhoushi
100410500   安阳市 ays anyangshi
100410501   市辖区 sxq shixiaqu
100410502   文峰区 wfq wenfengqu
100410503   北关区 bgq beiguanqu
100410505   殷都区 ydq yindouqu
100410506   龙安区 laq longanqu
100410522   安阳县 ayx anyangxian
100410523   汤阴县 tyx tangyinxian
100410526   滑县  hx  huaxian
100410527   内黄县 nhx neihuangxian
100410581   林州市 lzs linzhoushi
100410600   鹤壁市 hbs hebishi
100410601   市辖区 sxq shixiaqu
100410602   鹤山区 hsq heshanqu
100410603   山城区 scq shanchengqu
100410611   淇滨区 qbq qibinqu
100410621   浚县  jx  junxian
100410622   淇县  qx  qixian
100410700   新乡市 xxs xinxiangshi
100410701   市辖区 sxq shixiaqu
100410702   红旗区 hqq hongqiqu
100410703   卫滨区 wbq weibinqu
100410704   凤泉区 fqq fengquanqu
100410711   牧野区 myq muyequ
100410721   新乡县 xxx xinxiangxian
100410724   获嘉县 hjx huojiaxian
100410725   原阳县 yyx yuanyangxian
100410726   延津县 yjx yanjinxian
100410727   封丘县 fqx fengqiuxian
100410728   长垣县 zyx zhangyuanxian
100410781   卫辉市 whs weihuishi
100410782   辉县市 hxs huixianshi
100410800   焦作市 jzs jiaozuoshi
100410801   市辖区 sxq shixiaqu
100410802   解放区 jfq jiefangqu
100410803   中站区 zzq zhongzhanqu
100410804   马村区 mcq macunqu
100410811   山阳区 syq shanyangqu
100410821   修武县 xwx xiuwuxian
100410822   博爱县 bax boaixian
100410823   武陟县 wzx wuzhixian
100410825   温县  wx  wenxian
100410882   沁阳市 qys qinyangshi
100410883   孟州市 mzs mengzhoushi
100410900   濮阳市 pys puyangshi
100410901   市辖区 sxq shixiaqu
100410902   华龙区 hlq hualongqu
100410922   清丰县 qfx qingfengxian
100410923   南乐县 nlx nanlexian
100410926   范县  fx  fanxian
100410927   台前县 tqx taiqianxian
100410928   濮阳县 pyx puyangxian
100411000   许昌市 xcs xuchangshi
100411001   市辖区 sxq shixiaqu
100411002   魏都区 wdq weidouqu
100411023   许昌县 xcx xuchangxian
100411024   鄢陵县 ylx yanlingxian
100411025   襄城县 xcx xiangchengxian
100411081   禹州市 yzs yuzhoushi
100411082   长葛市 zgs zhanggeshi
100411100   漯河市 lhs luoheshi
100411101   市辖区 sxq shixiaqu
100411102   源汇区 yhq yuanhuiqu
100411103   郾城区 ycq yanchengqu
100411104   召陵区 zlq zhaolingqu
100411121   舞阳县 wyx wuyangxian
100411122   临颍县 lyx linyingxian
100411200   三门峡市    smxs    sanmenxiashi
100411201   市辖区 sxq shixiaqu
100411202   湖滨区 hbq hubinqu
100411221   渑池县 mcx mianchixian
100411222   陕县  sx  shanxian
100411224   卢氏县 lsx lushixian
100411281   义马市 yms yimashi
100411282   灵宝市 lbs lingbaoshi
100411300   南阳市 nys nanyangshi
100411301   市辖区 sxq shixiaqu
100411302   宛城区 wcq wanchengqu
100411303   卧龙区 wlq wolongqu
100411321   南召县 nzx nanzhaoxian
100411322   方城县 fcx fangchengxian
100411323   西峡县 xxx xixiaxian
100411324   镇平县 zpx zhenpingxian
100411325   内乡县 nxx neixiangxian
100411326   淅川县 xcx xichuanxian
100411327   社旗县 sqx sheqixian
100411328   唐河县 thx tanghexian
100411329   新野县 xyx xinyexian
100411330   桐柏县 tbx tongboxian
100411381   邓州市 dzs dengzhoushi
100411400   商丘市 sqs shangqiushi
100411401   市辖区 sxq shixiaqu
100411402   梁园区 lyq liangyuanqu
100411403   睢阳区 syq suiyangqu
100411421   民权县 mqx minquanxian
100411422   睢县  sx  suixian
100411423   宁陵县 nlx ninglingxian
100411424   柘城县 zcx zhechengxian
100411425   虞城县 ycx yuchengxian
100411426   夏邑县 xyx xiayixian
100411481   永城市 ycs yongchengshi
100411500   信阳市 xys xinyangshi
100411501   市辖区 sxq shixiaqu
100411502   浉河区 shq shihequ
100411503   平桥区 pqq pingqiaoqu
100411521   罗山县 lsx luoshanxian
100411522   光山县 gsx guangshanxian
100411523   新县  xx  xinxian
100411524   商城县 scx shangchengxian
100411525   固始县 gsx gushixian
100411526   潢川县 hcx huangchuanxian
100411527   淮滨县 hbx huaibinxian
100411528   息县  xx  xixian
100411600   周口市 zks zhoukoushi
100411601   市辖区 sxq shixiaqu
100411602   川汇区 chq chuanhuiqu
100411621   扶沟县 fgx fugouxian
100411622   西华县 xhx xihuaxian
100411623   商水县 ssx shangshuixian
100411624   沈丘县 sqx shenqiuxian
100411625   郸城县 dcx danchengxian
100411626   淮阳县 hyx huaiyangxian
100411627   太康县 tkx taikangxian
100411628   鹿邑县 lyx luyixian
100411681   项城市 xcs xiangchengshi
100411700   驻马店市    zmds    zhumadianshi
100411701   市辖区 sxq shixiaqu
100411702   驿城区 ycq yichengqu
100411721   西平县 xpx xipingxian
100411722   上蔡县 scx shangcaixian
100411723   平舆县 pyx pingyuxian
100411724   正阳县 zyx zhengyangxian
100411725   确山县 qsx queshanxian
100411726   泌阳县 myx miyangxian
100411727   汝南县 rnx runanxian
100411728   遂平县 spx suipingxian
100411729   新蔡县 xcx xincaixian
100419000   省直辖县级行政区划   szxxjxzqh   shengzhixiaxianjixingzhengquhua
100419001   济源市 jys jiyuanshi
100420000   湖北省 hbs hubeisheng
100420100   武汉市 whs wuhanshi
100420101   市辖区 sxq shixiaqu
100420102   江岸区 jaq jianganqu
100420103   江汉区 jhq jianghanqu
100420104   硚口区 qkq qiaokouqu
100420105   汉阳区 hyq hanyangqu
100420106   武昌区 wcq wuchangqu
100420107   青山区 qsq qingshanqu
100420111   洪山区 hsq hongshanqu
100420112   东西湖区    dxhq    dongxihuqu
100420113   汉南区 hnq hannanqu
100420114   蔡甸区 cdq caidianqu
100420115   江夏区 jxq jiangxiaqu
100420116   黄陂区 hpq huangpoqu
100420117   新洲区 xzq xinzhouqu
100420200   黄石市 hss huangshishi
100420201   市辖区 sxq shixiaqu
100420202   黄石港区    hsgq    huangshigangqu
100420203   西塞山区    xssq    xisaishanqu
100420204   下陆区 xlq xialuqu
100420205   铁山区 tsq tieshanqu
100420222   阳新县 yxx yangxinxian
100420281   大冶市 dys dayeshi
100420300   十堰市 sys shiyanshi
100420301   市辖区 sxq shixiaqu
100420302   茅箭区 mjq maojianqu
100420303   张湾区 zwq zhangwanqu
100420304   郧阳区 yyq yunyangqu
100420322   郧西县 yxx yunxixian
100420323   竹山县 zsx zhushanxian
100420324   竹溪县 zxx zhuxixian
100420325   房县  fx  fangxian
100420381   丹江口市    djks    danjiangkoushi
100420500   宜昌市 ycs yichangshi
100420501   市辖区 sxq shixiaqu
100420502   西陵区 xlq xilingqu
100420503   伍家岗区    wjgq    wujiagangqu
100420504   点军区 djq dianjunqu
100420505   猇亭区 ytq yaotingqu
100420506   夷陵区 ylq yilingqu
100420525   远安县 yax yuananxian
100420526   兴山县 xsx xingshanxian
100420527   秭归县 zgx ziguixian
100420528   长阳土家族自治县    zytjzzzx    zhangyangtujiazuzizhixian
100420529   五峰土家族自治县    wftjzzzx    wufengtujiazuzizhixian
100420581   宜都市 yds yidoushi
100420582   当阳市 dys dangyangshi
100420583   枝江市 zjs zhijiangshi
100420600   襄阳市 xys xiangyangshi
100420601   市辖区 sxq shixiaqu
100420602   襄城区 xcq xiangchengqu
100420606   樊城区 fcq fanchengqu
100420607   襄州区 xzq xiangzhouqu
100420624   南漳县 nzx nanzhangxian
100420625   谷城县 gcx guchengxian
100420626   保康县 bkx baokangxian
100420682   老河口市    lhks    laohekoushi
100420683   枣阳市 zys zaoyangshi
100420684   宜城市 ycs yichengshi
100420700   鄂州市 ezs ezhoushi
100420701   市辖区 sxq shixiaqu
100420702   梁子湖区    lzhq    liangzihuqu
100420703   华容区 hrq huarongqu
100420704   鄂城区 ecq echengqu
100420800   荆门市 jms jingmenshi
100420801   市辖区 sxq shixiaqu
100420802   东宝区 dbq dongbaoqu
100420804   掇刀区 ddq duodaoqu
100420821   京山县 jsx jingshanxian
100420822   沙洋县 syx shayangxian
100420881   钟祥市 zxs zhongxiangshi
100420900   孝感市 xgs xiaoganshi
100420901   市辖区 sxq shixiaqu
100420902   孝南区 xnq xiaonanqu
100420921   孝昌县 xcx xiaochangxian
100420922   大悟县 dwx dawuxian
100420923   云梦县 ymx yunmengxian
100420981   应城市 ycs yingchengshi
100420982   安陆市 als anlushi
100420984   汉川市 hcs hanchuanshi
100421000   荆州市 jzs jingzhoushi
100421001   市辖区 sxq shixiaqu
100421002   沙市区 ssq shashiqu
100421003   荆州区 jzq jingzhouqu
100421022   公安县 gax gonganxian
100421023   监利县 jlx jianlixian
100421024   江陵县 jlx jianglingxian
100421081   石首市 sss shishoushi
100421083   洪湖市 hhs honghushi
100421087   松滋市 szs songzishi
100421100   黄冈市 hgs huanggangshi
100421101   市辖区 sxq shixiaqu
100421102   黄州区 hzq huangzhouqu
100421121   团风县 tfx tuanfengxian
100421122   红安县 hax honganxian
100421123   罗田县 ltx luotianxian
100421124   英山县 ysx yingshanxian
100421125   浠水县 xsx xishuixian
100421126   蕲春县 qcx qichunxian
100421127   黄梅县 hmx huangmeixian
100421181   麻城市 mcs machengshi
100421182   武穴市 wxs wuxueshi
100421200   咸宁市 xns xianningshi
100421201   市辖区 sxq shixiaqu
100421202   咸安区 xaq xiananqu
100421221   嘉鱼县 jyx jiayuxian
100421222   通城县 tcx tongchengxian
100421223   崇阳县 cyx chongyangxian
100421224   通山县 tsx tongshanxian
100421281   赤壁市 cbs chibishi
100421300   随州市 szs suizhoushi
100421301   市辖区 sxq shixiaqu
100421303   曾都区 cdq cengdouqu
100421321   随县  sx  suixian
100421381   广水市 gss guangshuishi
100422800   恩施土家族苗族自治州  estjzmzzzz  enshitujiazumiaozuzizhizhou
100422801   恩施市 ess enshishi
100422802   利川市 lcs lichuanshi
100422822   建始县 jsx jianshixian
100422823   巴东县 bdx badongxian
100422825   宣恩县 xex xuanenxian
100422826   咸丰县 xfx xianfengxian
100422827   来凤县 lfx laifengxian
100422828   鹤峰县 hfx hefengxian
100429000   省直辖县级行政区划   szxxjxzqh   shengzhixiaxianjixingzhengquhua
100429004   仙桃市 xts xiantaoshi
100429005   潜江市 qjs qianjiangshi
100429006   天门市 tms tianmenshi
100429021   神农架林区   snjlq   shennongjialinqu
100430000   湖南省 hns hunansheng
100430100   长沙市 zss zhangshashi
100430101   市辖区 sxq shixiaqu
100430102   芙蓉区 frq furongqu
100430103   天心区 txq tianxinqu
100430104   岳麓区 ylq yueluqu
100430105   开福区 kfq kaifuqu
100430111   雨花区 yhq yuhuaqu
100430112   望城区 wcq wangchengqu
100430121   长沙县 zsx zhangshaxian
100430124   宁乡县 nxx ningxiangxian
100430181   浏阳市 lys liuyangshi
100430200   株洲市 zzs zhuzhoushi
100430201   市辖区 sxq shixiaqu
100430202   荷塘区 htq hetangqu
100430203   芦淞区 lsq lusongqu
100430204   石峰区 sfq shifengqu
100430211   天元区 tyq tianyuanqu
100430221   株洲县 zzx zhuzhouxian
100430223   攸县  yx  youxian
100430224   茶陵县 clx chalingxian
100430225   炎陵县 ylx yanlingxian
100430281   醴陵市 lls lilingshi
100430300   湘潭市 xts xiangtanshi
100430301   市辖区 sxq shixiaqu
100430302   雨湖区 yhq yuhuqu
100430304   岳塘区 ytq yuetangqu
100430321   湘潭县 xtx xiangtanxian
100430381   湘乡市 xxs xiangxiangshi
100430382   韶山市 sss shaoshanshi
100430400   衡阳市 hys hengyangshi
100430401   市辖区 sxq shixiaqu
100430405   珠晖区 zhq zhuhuiqu
100430406   雁峰区 yfq yanfengqu
100430407   石鼓区 sgq shiguqu
100430408   蒸湘区 zxq zhengxiangqu
100430412   南岳区 nyq nanyuequ
100430421   衡阳县 hyx hengyangxian
100430422   衡南县 hnx hengnanxian
100430423   衡山县 hsx hengshanxian
100430424   衡东县 hdx hengdongxian
100430426   祁东县 qdx qidongxian
100430481   耒阳市 lys leiyangshi
100430482   常宁市 cns changningshi
100430500   邵阳市 sys shaoyangshi
100430501   市辖区 sxq shixiaqu
100430502   双清区 sqq shuangqingqu
100430503   大祥区 dxq daxiangqu
100430511   北塔区 btq beitaqu
100430521   邵东县 sdx shaodongxian
100430522   新邵县 xsx xinshaoxian
100430523   邵阳县 syx shaoyangxian
100430524   隆回县 lhx longhuixian
100430525   洞口县 dkx dongkouxian
100430527   绥宁县 snx suiningxian
100430528   新宁县 xnx xinningxian
100430529   城步苗族自治县 cbmzzzx chengbumiaozuzizhixian
100430581   武冈市 wgs wugangshi
100430600   岳阳市 yys yueyangshi
100430601   市辖区 sxq shixiaqu
100430602   岳阳楼区    yylq    yueyanglouqu
100430603   云溪区 yxq yunxiqu
100430611   君山区 jsq junshanqu
100430621   岳阳县 yyx yueyangxian
100430623   华容县 hrx huarongxian
100430624   湘阴县 xyx xiangyinxian
100430626   平江县 pjx pingjiangxian
100430681   汨罗市 mls miluoshi
100430682   临湘市 lxs linxiangshi
100430700   常德市 cds changdeshi
100430701   市辖区 sxq shixiaqu
100430702   武陵区 wlq wulingqu
100430703   鼎城区 dcq dingchengqu
100430721   安乡县 axx anxiangxian
100430722   汉寿县 hsx hanshouxian
100430723   澧县  lx  lixian
100430724   临澧县 llx linlixian
100430725   桃源县 tyx taoyuanxian
100430726   石门县 smx shimenxian
100430781   津市市 jss jinshishi
100430800   张家界市    zjjs    zhangjiajieshi
100430801   市辖区 sxq shixiaqu
100430802   永定区 ydq yongdingqu
100430811   武陵源区    wlyq    wulingyuanqu
100430821   慈利县 clx cilixian
100430822   桑植县 szx sangzhixian
100430900   益阳市 yys yiyangshi
100430901   市辖区 sxq shixiaqu
100430902   资阳区 zyq ziyangqu
100430903   赫山区 hsq heshanqu
100430921   南县  nx  nanxian
100430922   桃江县 tjx taojiangxian
100430923   安化县 ahx anhuaxian
100430981   沅江市 yjs yuanjiangshi
100431000   郴州市 czs chenzhoushi
100431001   市辖区 sxq shixiaqu
100431002   北湖区 bhq beihuqu
100431003   苏仙区 sxq suxianqu
100431021   桂阳县 gyx guiyangxian
100431022   宜章县 yzx yizhangxian
100431023   永兴县 yxx yongxingxian
100431024   嘉禾县 jhx jiahexian
100431025   临武县 lwx linwuxian
100431026   汝城县 rcx ruchengxian
100431027   桂东县 gdx guidongxian
100431028   安仁县 arx anrenxian
100431081   资兴市 zxs zixingshi
100431100   永州市 yzs yongzhoushi
100431101   市辖区 sxq shixiaqu
100431102   零陵区 llq linglingqu
100431103   冷水滩区    lstq    lengshuitanqu
100431121   祁阳县 qyx qiyangxian
100431122   东安县 dax donganxian
100431123   双牌县 spx shuangpaixian
100431124   道县  dx  daoxian
100431125   江永县 jyx jiangyongxian
100431126   宁远县 nyx ningyuanxian
100431127   蓝山县 lsx lanshanxian
100431128   新田县 xtx xintianxian
100431129   江华瑶族自治县 jhyzzzx jianghuayaozuzizhixian
100431200   怀化市 hhs huaihuashi
100431201   市辖区 sxq shixiaqu
100431202   鹤城区 hcq hechengqu
100431221   中方县 zfx zhongfangxian
100431222   沅陵县 ylx yuanlingxian
100431223   辰溪县 cxx chenxixian
100431224   溆浦县 xpx xupuxian
100431225   会同县 htx huitongxian
100431226   麻阳苗族自治县 mymzzzx mayangmiaozuzizhixian
100431227   新晃侗族自治县 xhdzzzx xinhuangdongzuzizhixian
100431228   芷江侗族自治县 zjdzzzx zhijiangdongzuzizhixian
100431229   靖州苗族侗族自治县   jzmzdzzzx   jingzhoumiaozudongzuzizhixian
100431230   通道侗族自治县 tddzzzx tongdaodongzuzizhixian
100431281   洪江市 hjs hongjiangshi
100431300   娄底市 lds loudishi
100431301   市辖区 sxq shixiaqu
100431302   娄星区 lxq louxingqu
100431321   双峰县 sfx shuangfengxian
100431322   新化县 xhx xinhuaxian
100431381   冷水江市    lsjs    lengshuijiangshi
100431382   涟源市 lys lianyuanshi
100433100   湘西土家族苗族自治州  xxtjzmzzzz  xiangxitujiazumiaozuzizhizhou
100433101   吉首市 jss jishoushi
100433122   泸溪县 lxx luxixian
100433123   凤凰县 fhx fenghuangxian
100433124   花垣县 hyx huayuanxian
100433125   保靖县 bjx baojingxian
100433126   古丈县 gzx guzhangxian
100433127   永顺县 ysx yongshunxian
100433130   龙山县 lsx longshanxian
100440000   广东省 gds guangdongsheng
100440100   广州市 gzs guangzhoushi
100440101   市辖区 sxq shixiaqu
100440103   荔湾区 lwq liwanqu
100440104   越秀区 yxq yuexiuqu
100440105   海珠区 hzq haizhuqu
100440106   天河区 thq tianhequ
100440111   白云区 byq baiyunqu
100440112   黄埔区 hpq huangpuqu
100440113   番禺区 fyq fanyuqu
100440114   花都区 hdq huadouqu
100440115   南沙区 nsq nanshaqu
100440116   萝岗区 lgq luogangqu
100440117   从化区 chq conghuaqu
100440118   增城区 zcq zengchengqu
100440200   韶关市 sgs shaoguanshi
100440201   市辖区 sxq shixiaqu
100440203   武江区 wjq wujiangqu
100440204   浈江区 zjq zhenjiangqu
100440205   曲江区 qjq qujiangqu
100440222   始兴县 sxx shixingxian
100440224   仁化县 rhx renhuaxian
100440229   翁源县 wyx wengyuanxian
100440232   乳源瑶族自治县 ryyzzzx ruyuanyaozuzizhixian
100440233   新丰县 xfx xinfengxian
100440281   乐昌市 lcs lechangshi
100440282   南雄市 nxs nanxiongshi
100440300   深圳市 szs shenzhenshi
100440301   市辖区 sxq shixiaqu
100440303   罗湖区 lhq luohuqu
100440304   福田区 ftq futianqu
100440305   南山区 nsq nanshanqu
100440306   宝安区 baq baoanqu
100440307   龙岗区 lgq longgangqu
100440308   盐田区 ytq yantianqu
100440400   珠海市 zhs zhuhaishi
100440401   市辖区 sxq shixiaqu
100440402   香洲区 xzq xiangzhouqu
100440403   斗门区 dmq doumenqu
100440404   金湾区 jwq jinwanqu
100440500   汕头市 sts shantoushi
100440501   市辖区 sxq shixiaqu
100440507   龙湖区 lhq longhuqu
100440511   金平区 jpq jinpingqu
100440512   濠江区 hjq haojiangqu
100440513   潮阳区 cyq chaoyangqu
100440514   潮南区 cnq chaonanqu
100440515   澄海区 chq chenghaiqu
100440523   南澳县 nax nanaoxian
100440600   佛山市 fss foshanshi
100440601   市辖区 sxq shixiaqu
100440604   禅城区 scq shanchengqu
100440605   南海区 nhq nanhaiqu
100440606   顺德区 sdq shundequ
100440607   三水区 ssq sanshuiqu
100440608   高明区 gmq gaomingqu
100440700   江门市 jms jiangmenshi
100440701   市辖区 sxq shixiaqu
100440703   蓬江区 pjq pengjiangqu
100440704   江海区 jhq jianghaiqu
100440705   新会区 xhq xinhuiqu
100440781   台山市 tss taishanshi
100440783   开平市 kps kaipingshi
100440784   鹤山市 hss heshanshi
100440785   恩平市 eps enpingshi
100440800   湛江市 zjs zhanjiangshi
100440801   市辖区 sxq shixiaqu
100440802   赤坎区 ckq chikanqu
100440803   霞山区 xsq xiashanqu
100440804   坡头区 ptq potouqu
100440811   麻章区 mzq mazhangqu
100440823   遂溪县 sxx suixixian
100440825   徐闻县 xwx xuwenxian
100440881   廉江市 ljs lianjiangshi
100440882   雷州市 lzs leizhoushi
100440883   吴川市 wcs wuchuanshi
100440900   茂名市 mms maomingshi
100440901   市辖区 sxq shixiaqu
100440902   茂南区 mnq maonanqu
100440904   电白区 dbq dianbaiqu
100440981   高州市 gzs gaozhoushi
100440982   化州市 hzs huazhoushi
100440983   信宜市 xys xinyishi
100441200   肇庆市 zqs zhaoqingshi
100441201   市辖区 sxq shixiaqu
100441202   端州区 dzq duanzhouqu
100441203   鼎湖区 dhq dinghuqu
100441223   广宁县 gnx guangningxian
100441224   怀集县 hjx huaijixian
100441225   封开县 fkx fengkaixian
100441226   德庆县 dqx deqingxian
100441283   高要市 gys gaoyaoshi
100441284   四会市 shs sihuishi
100441300   惠州市 hzs huizhoushi
100441301   市辖区 sxq shixiaqu
100441302   惠城区 hcq huichengqu
100441303   惠阳区 hyq huiyangqu
100441322   博罗县 blx boluoxian
100441323   惠东县 hdx huidongxian
100441324   龙门县 lmx longmenxian
100441400   梅州市 mzs meizhoushi
100441401   市辖区 sxq shixiaqu
100441402   梅江区 mjq meijiangqu
100441403   梅县区 mxq meixianqu
100441422   大埔县 dpx dapuxian
100441423   丰顺县 fsx fengshunxian
100441424   五华县 whx wuhuaxian
100441426   平远县 pyx pingyuanxian
100441427   蕉岭县 jlx jiaolingxian
100441481   兴宁市 xns xingningshi
100441500   汕尾市 sws shanweishi
100441501   市辖区 sxq shixiaqu
100441502   城区  cq  chengqu
100441521   海丰县 hfx haifengxian
100441523   陆河县 lhx luhexian
100441581   陆丰市 lfs lufengshi
100441600   河源市 hys heyuanshi
100441601   市辖区 sxq shixiaqu
100441602   源城区 ycq yuanchengqu
100441621   紫金县 zjx zijinxian
100441622   龙川县 lcx longchuanxian
100441623   连平县 lpx lianpingxian
100441624   和平县 hpx hepingxian
100441625   东源县 dyx dongyuanxian
100441700   阳江市 yjs yangjiangshi
100441701   市辖区 sxq shixiaqu
100441702   江城区 jcq jiangchengqu
100441721   阳西县 yxx yangxixian
100441723   阳东县 ydx yangdongxian
100441781   阳春市 ycs yangchunshi
100441800   清远市 qys qingyuanshi
100441801   市辖区 sxq shixiaqu
100441802   清城区 qcq qingchengqu
100441803   清新区 qxq qingxinqu
100441821   佛冈县 fgx fogangxian
100441823   阳山县 ysx yangshanxian
100441825   连山壮族瑶族自治县   lszzyzzzx   lianshanzhuangzuyaozuzizhixian
100441826   连南瑶族自治县 lnyzzzx liannanyaozuzizhixian
100441881   英德市 yds yingdeshi
100441882   连州市 lzs lianzhoushi
100441900   东莞市 dgs dongguanshi
100442000   中山市 zss zhongshanshi
100445100   潮州市 czs chaozhoushi
100445101   市辖区 sxq shixiaqu
100445102   湘桥区 xqq xiangqiaoqu
100445103   潮安区 caq chaoanqu
100445122   饶平县 rpx raopingxian
100445200   揭阳市 jys jieyangshi
100445201   市辖区 sxq shixiaqu
100445202   榕城区 rcq rongchengqu
100445203   揭东区 jdq jiedongqu
100445222   揭西县 jxx jiexixian
100445224   惠来县 hlx huilaixian
100445281   普宁市 pns puningshi
100445300   云浮市 yfs yunfushi
100445301   市辖区 sxq shixiaqu
100445302   云城区 ycq yunchengqu
100445303   云安区 yaq yunanqu
100445321   新兴县 xxx xinxingxian
100445322   郁南县 ynx yunanxian
100445381   罗定市 lds luodingshi
100450000   广西壮族自治区 gxzzzzq guangxizhuangzuzizhiqu
100450100   南宁市 nns nanningshi
100450101   市辖区 sxq shixiaqu
100450102   兴宁区 xnq xingningqu
100450103   青秀区 qxq qingxiuqu
100450105   江南区 jnq jiangnanqu
100450107   西乡塘区    xxtq    xixiangtangqu
100450108   良庆区 lqq liangqingqu
100450109   邕宁区 ynq yongningqu
100450122   武鸣县 wmx wumingxian
100450123   隆安县 lax longanxian
100450124   马山县 msx mashanxian
100450125   上林县 slx shanglinxian
100450126   宾阳县 byx binyangxian
100450127   横县  hx  hengxian
100450200   柳州市 lzs liuzhoushi
100450201   市辖区 sxq shixiaqu
100450202   城中区 czq chengzhongqu
100450203   鱼峰区 yfq yufengqu
100450204   柳南区 lnq liunanqu
100450205   柳北区 lbq liubeiqu
100450221   柳江县 ljx liujiangxian
100450222   柳城县 lcx liuchengxian
100450223   鹿寨县 lzx luzhaixian
100450224   融安县 rax ronganxian
100450225   融水苗族自治县 rsmzzzx rongshuimiaozuzizhixian
100450226   三江侗族自治县 sjdzzzx sanjiangdongzuzizhixian
100450300   桂林市 gls guilinshi
100450301   市辖区 sxq shixiaqu
100450302   秀峰区 xfq xiufengqu
100450303   叠彩区 dcq diecaiqu
100450304   象山区 xsq xiangshanqu
100450305   七星区 qxq qixingqu
100450311   雁山区 ysq yanshanqu
100450312   临桂区 lgq linguiqu
100450321   阳朔县 ysx yangshuoxian
100450323   灵川县 lcx lingchuanxian
100450324   全州县 qzx quanzhouxian
100450325   兴安县 xax xinganxian
100450326   永福县 yfx yongfuxian
100450327   灌阳县 gyx guanyangxian
100450328   龙胜各族自治县 lsgzzzx longshenggezuzizhixian
100450329   资源县 zyx ziyuanxian
100450330   平乐县 plx pinglexian
100450331   荔浦县 lpx lipuxian
100450332   恭城瑶族自治县 gcyzzzx gongchengyaozuzizhixian
100450400   梧州市 wzs wuzhoushi
100450401   市辖区 sxq shixiaqu
100450403   万秀区 wxq wanxiuqu
100450405   长洲区 zzq zhangzhouqu
100450406   龙圩区 lwq longweiqu
100450421   苍梧县 cwx cangwuxian
100450422   藤县  tx  tengxian
100450423   蒙山县 msx mengshanxian
100450481   岑溪市 cxs cenxishi
100450500   北海市 bhs beihaishi
100450501   市辖区 sxq shixiaqu
100450502   海城区 hcq haichengqu
100450503   银海区 yhq yinhaiqu
100450512   铁山港区    tsgq    tieshangangqu
100450521   合浦县 hpx hepuxian
100450600   防城港市    fcgs    fangchenggangshi
100450601   市辖区 sxq shixiaqu
100450602   港口区 gkq gangkouqu
100450603   防城区 fcq fangchengqu
100450621   上思县 ssx shangsixian
100450681   东兴市 dxs dongxingshi
100450700   钦州市 qzs qinzhoushi
100450701   市辖区 sxq shixiaqu
100450702   钦南区 qnq qinnanqu
100450703   钦北区 qbq qinbeiqu
100450721   灵山县 lsx lingshanxian
100450722   浦北县 pbx pubeixian
100450800   贵港市 ggs guigangshi
100450801   市辖区 sxq shixiaqu
100450802   港北区 gbq gangbeiqu
100450803   港南区 gnq gangnanqu
100450804   覃塘区 ttq tantangqu
100450821   平南县 pnx pingnanxian
100450881   桂平市 gps guipingshi
100450900   玉林市 yls yulinshi
100450901   市辖区 sxq shixiaqu
100450902   玉州区 yzq yuzhouqu
100450903   福绵区 fmq fumianqu
100450921   容县  rx  rongxian
100450922   陆川县 lcx luchuanxian
100450923   博白县 bbx bobaixian
100450924   兴业县 xyx xingyexian
100450981   北流市 bls beiliushi
100451000   百色市 bss baiseshi
100451001   市辖区 sxq shixiaqu
100451002   右江区 yjq youjiangqu
100451021   田阳县 tyx tianyangxian
100451022   田东县 tdx tiandongxian
100451023   平果县 pgx pingguoxian
100451024   德保县 dbx debaoxian
100451025   靖西县 jxx jingxixian
100451026   那坡县 npx neipoxian
100451027   凌云县 lyx lingyunxian
100451028   乐业县 lyx leyexian
100451029   田林县 tlx tianlinxian
100451030   西林县 xlx xilinxian
100451031   隆林各族自治县 llgzzzx longlingezuzizhixian
100451100   贺州市 hzs hezhoushi
100451101   市辖区 sxq shixiaqu
100451102   八步区 bbq babuqu
100451121   昭平县 zpx zhaopingxian
100451122   钟山县 zsx zhongshanxian
100451123   富川瑶族自治县 fcyzzzx fuchuanyaozuzizhixian
100451200   河池市 hcs hechishi
100451201   市辖区 sxq shixiaqu
100451202   金城江区    jcjq    jinchengjiangqu
100451221   南丹县 ndx nandanxian
100451222   天峨县 tex tianexian
100451223   凤山县 fsx fengshanxian
100451224   东兰县 dlx donglanxian
100451225   罗城仫佬族自治县    lcmlzzzx    luochengmulaozuzizhixian
100451226   环江毛南族自治县    hjmnzzzx    huanjiangmaonanzuzizhixian
100451227   巴马瑶族自治县 bmyzzzx bamayaozuzizhixian
100451228   都安瑶族自治县 dayzzzx douanyaozuzizhixian
100451229   大化瑶族自治县 dhyzzzx dahuayaozuzizhixian
100451281   宜州市 yzs yizhoushi
100451300   来宾市 lbs laibinshi
100451301   市辖区 sxq shixiaqu
100451302   兴宾区 xbq xingbinqu
100451321   忻城县 xcx xinchengxian
100451322   象州县 xzx xiangzhouxian
100451323   武宣县 wxx wuxuanxian
100451324   金秀瑶族自治县 jxyzzzx jinxiuyaozuzizhixian
100451381   合山市 hss heshanshi
100451400   崇左市 czs chongzuoshi
100451401   市辖区 sxq shixiaqu
100451402   江州区 jzq jiangzhouqu
100451421   扶绥县 fsx fusuixian
100451422   宁明县 nmx ningmingxian
100451423   龙州县 lzx longzhouxian
100451424   大新县 dxx daxinxian
100451425   天等县 tdx tiandengxian
100451481   凭祥市 pxs pingxiangshi
100460000   海南省 hns hainansheng
100460100   海口市 hks haikoushi
100460101   市辖区 sxq shixiaqu
100460105   秀英区 xyq xiuyingqu
100460106   龙华区 lhq longhuaqu
100460107   琼山区 qsq qiongshanqu
100460108   美兰区 mlq meilanqu
100460200   三亚市 sys sanyashi
100460201   市辖区 sxq shixiaqu
100460202   海棠区 htq haitangqu
100460203   吉阳区 jyq jiyangqu
100460204   天涯区 tyq tianyaqu
100460205   崖州区 yzq yazhouqu
100460300   三沙市 sss sanshashi
100469000   省直辖县级行政区划   szxxjxzqh   shengzhixiaxianjixingzhengquhua
100469001   五指山市    wzss    wuzhishanshi
100469002   琼海市 qhs qionghaishi
100469003   儋州市 dzs danzhoushi
100469005   文昌市 wcs wenchangshi
100469006   万宁市 wns wanningshi
100469007   东方市 dfs dongfangshi
100469021   定安县 dax dinganxian
100469022   屯昌县 tcx tunchangxian
100469023   澄迈县 cmx chengmaixian
100469024   临高县 lgx lingaoxian
100469025   白沙黎族自治县 bslzzzx baishalizuzizhixian
100469026   昌江黎族自治县 cjlzzzx changjianglizuzizhixian
100469027   乐东黎族自治县 ldlzzzx ledonglizuzizhixian
100469028   陵水黎族自治县 lslzzzx lingshuilizuzizhixian
100469029   保亭黎族苗族自治县   btlzmzzzx   baotinglizumiaozuzizhixian
100469030   琼中黎族苗族自治县   qzlzmzzzx   qiongzhonglizumiaozuzizhixian
100500000   重庆市 cq  chongqing
100500100   市辖区 sxq shixiaqu
100500101   万州区 wzq wanzhouqu
100500102   涪陵区 flq fulingqu
100500103   渝中区 yzq yuzhongqu
100500104   大渡口区    ddkq    dadukouqu
100500105   江北区 jbq jiangbeiqu
100500106   沙坪坝区    spbq    shapingbaqu
100500107   九龙坡区    jlpq    jiulongpoqu
100500108   南岸区 naq nananqu
100500109   北碚区 bbq beibeiqu
100500110   綦江区 qjq qijiangqu
100500111   大足区 dzq dazuqu
100500112   渝北区 ybq yubeiqu
100500113   巴南区 bnq bananqu
100500114   黔江区 qjq qianjiangqu
100500115   长寿区 zsq zhangshouqu
100500116   江津区 jjq jiangjinqu
100500117   合川区 hcq hechuanqu
100500118   永川区 ycq yongchuanqu
100500119   南川区 ncq nanchuanqu
100500120   璧山区 bsq bishanqu
100500151   铜梁区 tlq tongliangqu
100500200   县   x   xian
100500223   潼南县 tnx tongnanxian
100500226   荣昌县 rcx rongchangxian
100500228   梁平县 lpx liangpingxian
100500229   城口县 ckx chengkouxian
100500230   丰都县 fdx fengdouxian
100500231   垫江县 djx dianjiangxian
100500232   武隆县 wlx wulongxian
100500233   忠县  zx  zhongxian
100500234   开县  kx  kaixian
100500235   云阳县 yyx yunyangxian
100500236   奉节县 fjx fengjiexian
100500237   巫山县 wsx wushanxian
100500238   巫溪县 wxx wuxixian
100500240   石柱土家族自治县    sztjzzzx    shizhutujiazuzizhixian
100500241   秀山土家族苗族自治县  xstjzmzzzx  xiushantujiazumiaozuzizhixian
100500242   酉阳土家族苗族自治县  yytjzmzzzx  youyangtujiazumiaozuzizhixian
100500243   彭水苗族土家族自治县  psmztjzzzx  pengshuimiaozutujiazuzizhixian
100510000   四川省 scs sichuansheng
100510100   成都市 cds chengdoushi
100510101   市辖区 sxq shixiaqu
100510104   锦江区 jjq jinjiangqu
100510105   青羊区 qyq qingyangqu
100510106   金牛区 jnq jinniuqu
100510107   武侯区 whq wuhouqu
100510108   成华区 chq chenghuaqu
100510112   龙泉驿区    lqyq    longquanyiqu
100510113   青白江区    qbjq    qingbaijiangqu
100510114   新都区 xdq xindouqu
100510115   温江区 wjq wenjiangqu
100510121   金堂县 jtx jintangxian
100510122   双流县 slx shuangliuxian
100510124   郫县  px  pixian
100510129   大邑县 dyx dayixian
100510131   蒲江县 pjx pujiangxian
100510132   新津县 xjx xinjinxian
100510181   都江堰市    djys    doujiangyanshi
100510182   彭州市 pzs pengzhoushi
100510183   邛崃市 qls qionglaishi
100510184   崇州市 czs chongzhoushi
100510300   自贡市 zgs zigongshi
100510301   市辖区 sxq shixiaqu
100510302   自流井区    zljq    ziliujingqu
100510303   贡井区 gjq gongjingqu
100510304   大安区 daq daanqu
100510311   沿滩区 ytq yantanqu
100510321   荣县  rx  rongxian
100510322   富顺县 fsx fushunxian
100510400   攀枝花市    pzhs    panzhihuashi
100510401   市辖区 sxq shixiaqu
100510402   东区  dq  dongqu
100510403   西区  xq  xiqu
100510411   仁和区 rhq renhequ
100510421   米易县 myx miyixian
100510422   盐边县 ybx yanbianxian
100510500   泸州市 lzs luzhoushi
100510501   市辖区 sxq shixiaqu
100510502   江阳区 jyq jiangyangqu
100510503   纳溪区 nxq naxiqu
100510504   龙马潭区    lmtq    longmatanqu
100510521   泸县  lx  luxian
100510522   合江县 hjx hejiangxian
100510524   叙永县 xyx xuyongxian
100510525   古蔺县 glx gulinxian
100510600   德阳市 dys deyangshi
100510601   市辖区 sxq shixiaqu
100510603   旌阳区 jyq jingyangqu
100510623   中江县 zjx zhongjiangxian
100510626   罗江县 ljx luojiangxian
100510681   广汉市 ghs guanghanshi
100510682   什邡市 sfs shenfangshi
100510683   绵竹市 mzs mianzhushi
100510700   绵阳市 mys mianyangshi
100510701   市辖区 sxq shixiaqu
100510703   涪城区 fcq fuchengqu
100510704   游仙区 yxq youxianqu
100510722   三台县 stx santaixian
100510723   盐亭县 ytx yantingxian
100510724   安县  ax  anxian
100510725   梓潼县 ztx zitongxian
100510726   北川羌族自治县 bcqzzzx beichuanqiangzuzizhixian
100510727   平武县 pwx pingwuxian
100510781   江油市 jys jiangyoushi
100510800   广元市 gys guangyuanshi
100510801   市辖区 sxq shixiaqu
100510802   利州区 lzq lizhouqu
100510811   昭化区 zhq zhaohuaqu
100510812   朝天区 ctq chaotianqu
100510821   旺苍县 wcx wangcangxian
100510822   青川县 qcx qingchuanxian
100510823   剑阁县 jgx jiangexian
100510824   苍溪县 cxx cangxixian
100510900   遂宁市 sns suiningshi
100510901   市辖区 sxq shixiaqu
100510903   船山区 csq chuanshanqu
100510904   安居区 ajq anjuqu
100510921   蓬溪县 pxx pengxixian
100510922   射洪县 shx shehongxian
100510923   大英县 dyx dayingxian
100511000   内江市 njs neijiangshi
100511001   市辖区 sxq shixiaqu
100511002   市中区 szq shizhongqu
100511011   东兴区 dxq dongxingqu
100511024   威远县 wyx weiyuanxian
100511025   资中县 zzx zizhongxian
100511028   隆昌县 lcx longchangxian
100511100   乐山市 lss leshanshi
100511101   市辖区 sxq shixiaqu
100511102   市中区 szq shizhongqu
100511111   沙湾区 swq shawanqu
100511112   五通桥区    wtqq    wutongqiaoqu
100511113   金口河区    jkhq    jinkouhequ
100511123   犍为县 jwx jianweixian
100511124   井研县 jyx jingyanxian
100511126   夹江县 jjx jiajiangxian
100511129   沐川县 mcx muchuanxian
100511132   峨边彝族自治县 ebyzzzx ebianyizuzizhixian
100511133   马边彝族自治县 mbyzzzx mabianyizuzizhixian
100511181   峨眉山市    emss    emeishanshi
100511300   南充市 ncs nanchongshi
100511301   市辖区 sxq shixiaqu
100511302   顺庆区 sqq shunqingqu
100511303   高坪区 gpq gaopingqu
100511304   嘉陵区 jlq jialingqu
100511321   南部县 nbx nanbuxian
100511322   营山县 ysx yingshanxian
100511323   蓬安县 pax penganxian
100511324   仪陇县 ylx yilongxian
100511325   西充县 xcx xichongxian
100511381   阆中市 lzs langzhongshi
100511400   眉山市 mss meishanshi
100511401   市辖区 sxq shixiaqu
100511402   东坡区 dpq dongpoqu
100511421   仁寿县 rsx renshouxian
100511422   彭山县 psx pengshanxian
100511423   洪雅县 hyx hongyaxian
100511424   丹棱县 dlx danlengxian
100511425   青神县 qsx qingshenxian
100511500   宜宾市 ybs yibinshi
100511501   市辖区 sxq shixiaqu
100511502   翠屏区 cpq cuipingqu
100511503   南溪区 nxq nanxiqu
100511521   宜宾县 ybx yibinxian
100511523   江安县 jax jianganxian
100511524   长宁县 znx zhangningxian
100511525   高县  gx  gaoxian
100511526   珙县  gx  gongxian
100511527   筠连县 ylx yunlianxian
100511528   兴文县 xwx xingwenxian
100511529   屏山县 psx pingshanxian
100511600   广安市 gas guanganshi
100511601   市辖区 sxq shixiaqu
100511602   广安区 gaq guanganqu
100511603   前锋区 qfq qianfengqu
100511621   岳池县 ycx yuechixian
100511622   武胜县 wsx wushengxian
100511623   邻水县 lsx linshuixian
100511681   华蓥市 hys huayingshi
100511700   达州市 dzs dazhoushi
100511701   市辖区 sxq shixiaqu
100511702   通川区 tcq tongchuanqu
100511703   达川区 dcq dachuanqu
100511722   宣汉县 xhx xuanhanxian
100511723   开江县 kjx kaijiangxian
100511724   大竹县 dzx dazhuxian
100511725   渠县  qx  quxian
100511781   万源市 wys wanyuanshi
100511800   雅安市 yas yaanshi
100511801   市辖区 sxq shixiaqu
100511802   雨城区 ycq yuchengqu
100511803   名山区 msq mingshanqu
100511822   荥经县 yjx yingjingxian
100511823   汉源县 hyx hanyuanxian
100511824   石棉县 smx shimianxian
100511825   天全县 tqx tianquanxian
100511826   芦山县 lsx lushanxian
100511827   宝兴县 bxx baoxingxian
100511900   巴中市 bzs bazhongshi
100511901   市辖区 sxq shixiaqu
100511902   巴州区 bzq bazhouqu
100511903   恩阳区 eyq enyangqu
100511921   通江县 tjx tongjiangxian
100511922   南江县 njx nanjiangxian
100511923   平昌县 pcx pingchangxian
100512000   资阳市 zys ziyangshi
100512001   市辖区 sxq shixiaqu
100512002   雁江区 yjq yanjiangqu
100512021   安岳县 ayx anyuexian
100512022   乐至县 lzx lezhixian
100512081   简阳市 jys jianyangshi
100513200   阿坝藏族羌族自治州   abzzqzzzz   abazangzuqiangzuzizhizhou
100513221   汶川县 wcx wenchuanxian
100513222   理县  lx  lixian
100513223   茂县  mx  maoxian
100513224   松潘县 spx songpanxian
100513225   九寨沟县    jzgx    jiuzhaigouxian
100513226   金川县 jcx jinchuanxian
100513227   小金县 xjx xiaojinxian
100513228   黑水县 hsx heishuixian
100513229   马尔康县    mekx    maerkangxian
100513230   壤塘县 rtx rangtangxian
100513231   阿坝县 abx abaxian
100513232   若尔盖县    regx    ruoergaixian
100513233   红原县 hyx hongyuanxian
100513300   甘孜藏族自治州 gzzzzzz ganzizangzuzizhizhou
100513321   康定县 kdx kangdingxian
100513322   泸定县 ldx ludingxian
100513323   丹巴县 dbx danbaxian
100513324   九龙县 jlx jiulongxian
100513325   雅江县 yjx yajiangxian
100513326   道孚县 dfx daofuxian
100513327   炉霍县 lhx luhuoxian
100513328   甘孜县 gzx ganzixian
100513329   新龙县 xlx xinlongxian
100513330   德格县 dgx degexian
100513331   白玉县 byx baiyuxian
100513332   石渠县 sqx shiquxian
100513333   色达县 sdx sedaxian
100513334   理塘县 ltx litangxian
100513335   巴塘县 btx batangxian
100513336   乡城县 xcx xiangchengxian
100513337   稻城县 dcx daochengxian
100513338   得荣县 drx derongxian
100513400   凉山彝族自治州 lsyzzzz liangshanyizuzizhizhou
100513401   西昌市 xcs xichangshi
100513422   木里藏族自治县 mlzzzzx mulizangzuzizhixian
100513423   盐源县 yyx yanyuanxian
100513424   德昌县 dcx dechangxian
100513425   会理县 hlx huilixian
100513426   会东县 hdx huidongxian
100513427   宁南县 nnx ningnanxian
100513428   普格县 pgx pugexian
100513429   布拖县 btx butuoxian
100513430   金阳县 jyx jinyangxian
100513431   昭觉县 zjx zhaojuexian
100513432   喜德县 xdx xidexian
100513433   冕宁县 mnx mianningxian
100513434   越西县 yxx yuexixian
100513435   甘洛县 glx ganluoxian
100513436   美姑县 mgx meiguxian
100513437   雷波县 lbx leiboxian
100520000   贵州省 gzs guizhousheng
100520100   贵阳市 gys guiyangshi
100520101   市辖区 sxq shixiaqu
100520102   南明区 nmq nanmingqu
100520103   云岩区 yyq yunyanqu
100520111   花溪区 hxq huaxiqu
100520112   乌当区 wdq wudangqu
100520113   白云区 byq baiyunqu
100520115   观山湖区    gshq    guanshanhuqu
100520121   开阳县 kyx kaiyangxian
100520122   息烽县 xfx xifengxian
100520123   修文县 xwx xiuwenxian
100520181   清镇市 qzs qingzhenshi
100520200   六盘水市    lpss    liupanshuishi
100520201   钟山区 zsq zhongshanqu
100520203   六枝特区    lztq    liuzhitequ
100520221   水城县 scx shuichengxian
100520222   盘县  px  panxian
100520300   遵义市 zys zunyishi
100520301   市辖区 sxq shixiaqu
100520302   红花岗区    hhgq    honghuagangqu
100520303   汇川区 hcq huichuanqu
100520321   遵义县 zyx zunyixian
100520322   桐梓县 tzx tongzixian
100520323   绥阳县 syx suiyangxian
100520324   正安县 zax zhenganxian
100520325   道真仡佬族苗族自治县  dzglzmzzzx  daozhengelaozumiaozuzizhixian
100520326   务川仡佬族苗族自治县  wcglzmzzzx  wuchuangelaozumiaozuzizhixian
100520327   凤冈县 fgx fenggangxian
100520328   湄潭县 mtx meitanxian
100520329   余庆县 yqx yuqingxian
100520330   习水县 xsx xishuixian
100520381   赤水市 css chishuishi
100520382   仁怀市 rhs renhuaishi
100520400   安顺市 ass anshunshi
100520401   市辖区 sxq shixiaqu
100520402   西秀区 xxq xixiuqu
100520421   平坝县 pbx pingbaxian
100520422   普定县 pdx pudingxian
100520423   镇宁布依族苗族自治县  znbyzmzzzx  zhenningbuyizumiaozuzizhixian
100520424   关岭布依族苗族自治县  glbyzmzzzx  guanlingbuyizumiaozuzizhixian
100520425   紫云苗族布依族自治县  zymzbyzzzx  ziyunmiaozubuyizuzizhixian
100520500   毕节市 bjs bijieshi
100520501   市辖区 sxq shixiaqu
100520502   七星关区    qxgq    qixingguanqu
100520521   大方县 dfx dafangxian
100520522   黔西县 qxx qianxixian
100520523   金沙县 jsx jinshaxian
100520524   织金县 zjx zhijinxian
100520525   纳雍县 nyx nayongxian
100520526   威宁彝族回族苗族自治县 wnyzhzmzzzx weiningyizuhuizumiaozuzizhixian
100520527   赫章县 hzx hezhangxian
100520600   铜仁市 trs tongrenshi
100520601   市辖区 sxq shixiaqu
100520602   碧江区 bjq bijiangqu
100520603   万山区 wsq wanshanqu
100520621   江口县 jkx jiangkouxian
100520622   玉屏侗族自治县 ypdzzzx yupingdongzuzizhixian
100520623   石阡县 sqx shiqianxian
100520624   思南县 snx sinanxian
100520625   印江土家族苗族自治县  yjtjzmzzzx  yinjiangtujiazumiaozuzizhixian
100520626   德江县 djx dejiangxian
100520627   沿河土家族自治县    yhtjzzzx    yanhetujiazuzizhixian
100520628   松桃苗族自治县 stmzzzx songtaomiaozuzizhixian
100522300   黔西南布依族苗族自治州 qxnbyzmzzzz qianxinanbuyizumiaozuzizhizhou
100522301   兴义市 xys xingyishi
100522322   兴仁县 xrx xingrenxian
100522323   普安县 pax puanxian
100522324   晴隆县 qlx qinglongxian
100522325   贞丰县 zfx zhenfengxian
100522326   望谟县 wmx wangmoxian
100522327   册亨县 chx cehengxian
100522328   安龙县 alx anlongxian
100522600   黔东南苗族侗族自治州  qdnmzdzzzz  qiandongnanmiaozudongzuzizhizhou
100522601   凯里市 kls kailishi
100522622   黄平县 hpx huangpingxian
100522623   施秉县 sbx shibingxian
100522624   三穗县 ssx sansuixian
100522625   镇远县 zyx zhenyuanxian
100522626   岑巩县 cgx cengongxian
100522627   天柱县 tzx tianzhuxian
100522628   锦屏县 jpx jinpingxian
100522629   剑河县 jhx jianhexian
100522630   台江县 tjx taijiangxian
100522631   黎平县 lpx lipingxian
100522632   榕江县 rjx rongjiangxian
100522633   从江县 cjx congjiangxian
100522634   雷山县 lsx leishanxian
100522635   麻江县 mjx majiangxian
100522636   丹寨县 dzx danzhaixian
100522700   黔南布依族苗族自治州  qnbyzmzzzz  qiannanbuyizumiaozuzizhizhou
100522701   都匀市 dys douyunshi
100522702   福泉市 fqs fuquanshi
100522722   荔波县 lbx liboxian
100522723   贵定县 gdx guidingxian
100522725   瓮安县 wax wenganxian
100522726   独山县 dsx dushanxian
100522727   平塘县 ptx pingtangxian
100522728   罗甸县 ldx luodianxian
100522729   长顺县 zsx zhangshunxian
100522730   龙里县 llx longlixian
100522731   惠水县 hsx huishuixian
100522732   三都水族自治县 sdszzzx sandoushuizuzizhixian
100530000   云南省 yns yunnansheng
100530100   昆明市 kms kunmingshi
100530101   市辖区 sxq shixiaqu
100530102   五华区 whq wuhuaqu
100530103   盘龙区 plq panlongqu
100530111   官渡区 gdq guanduqu
100530112   西山区 xsq xishanqu
100530113   东川区 dcq dongchuanqu
100530114   呈贡区 cgq chenggongqu
100530122   晋宁县 jnx jinningxian
100530124   富民县 fmx fuminxian
100530125   宜良县 ylx yiliangxian
100530126   石林彝族自治县 slyzzzx shilinyizuzizhixian
100530127   嵩明县 smx songmingxian
100530128   禄劝彝族苗族自治县   lqyzmzzzx   luquanyizumiaozuzizhixian
100530129   寻甸回族彝族自治县   xdhzyzzzx   xundianhuizuyizuzizhixian
100530181   安宁市 ans anningshi
100530300   曲靖市 qjs qujingshi
100530301   市辖区 sxq shixiaqu
100530302   麒麟区 qlq qilinqu
100530321   马龙县 mlx malongxian
100530322   陆良县 llx luliangxian
100530323   师宗县 szx shizongxian
100530324   罗平县 lpx luopingxian
100530325   富源县 fyx fuyuanxian
100530326   会泽县 hzx huizexian
100530328   沾益县 zyx zhanyixian
100530381   宣威市 xws xuanweishi
100530400   玉溪市 yxs yuxishi
100530401   市辖区 sxq shixiaqu
100530402   红塔区 htq hongtaqu
100530421   江川县 jcx jiangchuanxian
100530422   澄江县 cjx chengjiangxian
100530423   通海县 thx tonghaixian
100530424   华宁县 hnx huaningxian
100530425   易门县 ymx yimenxian
100530426   峨山彝族自治县 esyzzzx eshanyizuzizhixian
100530427   新平彝族傣族自治县   xpyzdzzzx   xinpingyizudaizuzizhixian
100530428   元江哈尼族彝族傣族自治县    yjhnzyzdzzzx    yuanjianghanizuyizudaizuzizhixian
100530500   保山市 bss baoshanshi
100530501   市辖区 sxq shixiaqu
100530502   隆阳区 lyq longyangqu
100530521   施甸县 sdx shidianxian
100530522   腾冲县 tcx tengchongxian
100530523   龙陵县 llx longlingxian
100530524   昌宁县 cnx changningxian
100530600   昭通市 zts zhaotongshi
100530601   市辖区 sxq shixiaqu
100530602   昭阳区 zyq zhaoyangqu
100530621   鲁甸县 ldx ludianxian
100530622   巧家县 qjx qiaojiaxian
100530623   盐津县 yjx yanjinxian
100530624   大关县 dgx daguanxian
100530625   永善县 ysx yongshanxian
100530626   绥江县 sjx suijiangxian
100530627   镇雄县 zxx zhenxiongxian
100530628   彝良县 ylx yiliangxian
100530629   威信县 wxx CRMxian
100530630   水富县 sfx shuifuxian
100530700   丽江市 ljs lijiangshi
100530701   市辖区 sxq shixiaqu
100530702   古城区 gcq guchengqu
100530721   玉龙纳西族自治县    ylnxzzzx    yulongnaxizuzizhixian
100530722   永胜县 ysx yongshengxian
100530723   华坪县 hpx huapingxian
100530724   宁蒗彝族自治县 nlyzzzx ninglangyizuzizhixian
100530800   普洱市 pes puershi
100530801   市辖区 sxq shixiaqu
100530802   思茅区 smq simaoqu
100530821   宁洱哈尼族彝族自治县  nehnzyzzzx  ningerhanizuyizuzizhixian
100530822   墨江哈尼族自治县    mjhnzzzx    mojianghanizuzizhixian
100530823   景东彝族自治县 jdyzzzx jingdongyizuzizhixian
100530824   景谷傣族彝族自治县   jgdzyzzzx   jinggudaizuyizuzizhixian
100530825   镇沅彝族哈尼族拉祜族自治县   zyyzhnzlhzzzx   zhenyuanyizuhanizulahuzuzizhixian
100530826   江城哈尼族彝族自治县  jchnzyzzzx  jiangchenghanizuyizuzizhixian
100530827   孟连傣族拉祜族佤族自治县    mldzlhzwzzzx    mengliandaizulahuzuwazuzizhixian
100530828   澜沧拉祜族自治县    lclhzzzx    lancanglahuzuzizhixian
100530829   西盟佤族自治县 xmwzzzx ximengwazuzizhixian
100530900   临沧市 lcs lincangshi
100530901   市辖区 sxq shixiaqu
100530902   临翔区 lxq linxiangqu
100530921   凤庆县 fqx fengqingxian
100530922   云县  yx  yunxian
100530923   永德县 ydx yongdexian
100530924   镇康县 zkx zhenkangxian
100530926   耿马傣族佤族自治县   gmdzwzzzx   gengmadaizuwazuzizhixian
100530927   沧源佤族自治县 cywzzzx cangyuanwazuzizhixian
100532300   楚雄彝族自治州 cxyzzzz chuxiongyizuzizhizhou
100532301   楚雄市 cxs chuxiongshi
100532322   双柏县 sbx shuangboxian
100532323   牟定县 mdx moudingxian
100532324   南华县 nhx nanhuaxian
100532325   姚安县 yax yaoanxian
100532326   大姚县 dyx dayaoxian
100532327   永仁县 yrx yongrenxian
100532328   元谋县 ymx yuanmouxian
100532329   武定县 wdx wudingxian
100532331   禄丰县 lfx lufengxian
100532500   红河哈尼族彝族自治州  hhhnzyzzzz  honghehanizuyizuzizhizhou
100532501   个旧市 gjs gejiushi
100532502   开远市 kys kaiyuanshi
100532503   蒙自市 mzs mengzishi
100532504   弥勒市 mls mileshi
100532523   屏边苗族自治县 pbmzzzx pingbianmiaozuzizhixian
100532524   建水县 jsx jianshuixian
100532525   石屏县 spx shipingxian
100532527   泸西县 lxx luxixian
100532528   元阳县 yyx yuanyangxian
100532529   红河县 hhx honghexian
100532530   金平苗族瑶族傣族自治县 jpmzyzdzzzx jinpingmiaozuyaozudaizuzizhixian
100532531   绿春县 lcx lu:chunxian
100532532   河口瑶族自治县 hkyzzzx hekouyaozuzizhixian
100532600   文山壮族苗族自治州   wszzmzzzz   wenshanzhuangzumiaozuzizhizhou
100532601   文山市 wss wenshanshi
100532622   砚山县 ysx yanshanxian
100532623   西畴县 xcx xichouxian
100532624   麻栗坡县    mlpx    malipoxian
100532625   马关县 mgx maguanxian
100532626   丘北县 qbx qiubeixian
100532627   广南县 gnx guangnanxian
100532628   富宁县 fnx funingxian
100532800   西双版纳傣族自治州   xsbndzzzz   xishuangbannadaizuzizhizhou
100532801   景洪市 jhs jinghongshi
100532822   勐海县 mhx menghaixian
100532823   勐腊县 mlx menglaxian
100532900   大理白族自治州 dlbzzzz dalibaizuzizhizhou
100532901   大理市 dls dalishi
100532922   漾濞彝族自治县 ybyzzzx yangbiyizuzizhixian
100532923   祥云县 xyx xiangyunxian
100532924   宾川县 bcx binchuanxian
100532925   弥渡县 mdx miduxian
100532926   南涧彝族自治县 njyzzzx nanjianyizuzizhixian
100532927   巍山彝族回族自治县   wsyzhzzzx   weishanyizuhuizuzizhixian
100532928   永平县 ypx yongpingxian
100532929   云龙县 ylx yunlongxian
100532930   洱源县 eyx eryuanxian
100532931   剑川县 jcx jianchuanxian
100532932   鹤庆县 hqx heqingxian
100533100   德宏傣族景颇族自治州  dhdzjpzzzz  dehongdaizujingpozuzizhizhou
100533102   瑞丽市 rls ruilishi
100533103   芒市  ms  mangshi
100533122   梁河县 lhx lianghexian
100533123   盈江县 yjx yingjiangxian
100533124   陇川县 lcx longchuanxian
100533300   怒江傈僳族自治州    njlszzzz    nujianglisuzuzizhizhou
100533321   泸水县 lsx lushuixian
100533323   福贡县 fgx fugongxian
100533324   贡山独龙族怒族自治县  gsdlznzzzx  gongshandulongzunuzuzizhixian
100533325   兰坪白族普米族自治县  lpbzpmzzzx  lanpingbaizupumizuzizhixian
100533400   迪庆藏族自治州 dqzzzzz diqingzangzuzizhizhou
100533421   香格里拉县   xgllx   xianggelilaxian
100533422   德钦县 dqx deqinxian
100533423   维西傈僳族自治县    wxlszzzx    weixilisuzuzizhixian
100540000   西藏自治区   xzzzq   xizangzizhiqu
100540100   拉萨市 lss lasashi
100540101   市辖区 sxq shixiaqu
100540102   城关区 cgq chengguanqu
100540121   林周县 lzx linzhouxian
100540122   当雄县 dxx dangxiongxian
100540123   尼木县 nmx nimuxian
100540124   曲水县 qsx qushuixian
100540125   堆龙德庆县   dldqx   duilongdeqingxian
100540126   达孜县 dzx dazixian
100540127   墨竹工卡县   mzgkx   mozhugongkaxian
100540200   日喀则市    rkzs    rikazeshi
100540202   桑珠孜区    szzq    sangzhuziqu
100540221   南木林县    nmlx    nanmulinxian
100540222   江孜县 jzx jiangzixian
100540223   定日县 drx dingrixian
100540224   萨迦县 sjx sajiaxian
100540225   拉孜县 lzx lazixian
100540226   昂仁县 arx angrenxian
100540227   谢通门县    xtmx    xietongmenxian
100540228   白朗县 blx bailangxian
100540229   仁布县 rbx renbuxian
100540230   康马县 kmx kangmaxian
100540231   定结县 djx dingjiexian
100540232   仲巴县 zbx zhongbaxian
100540233   亚东县 ydx yadongxian
100540234   吉隆县 jlx jilongxian
100540235   聂拉木县    nlmx    nielamuxian
100540236   萨嘎县 sgx sagaxian
100540237   岗巴县 gbx gangbaxian
100542100   昌都地区    cddq    changdoudiqu
100542121   昌都县 cdx changdouxian
100542122   江达县 jdx jiangdaxian
100542123   贡觉县 gjx gongjuexian
100542124   类乌齐县    lwqx    leiwuqixian
100542125   丁青县 dqx dingqingxian
100542126   察雅县 cyx chayaxian
100542127   八宿县 bsx basuxian
100542128   左贡县 zgx zuogongxian
100542129   芒康县 mkx mangkangxian
100542132   洛隆县 llx luolongxian
100542133   边坝县 bbx bianbaxian
100542200   山南地区    sndq    shannandiqu
100542221   乃东县 ndx naidongxian
100542222   扎囊县 znx zhanangxian
100542223   贡嘎县 ggx gonggaxian
100542224   桑日县 srx sangrixian
100542225   琼结县 qjx qiongjiexian
100542226   曲松县 qsx qusongxian
100542227   措美县 cmx cuomeixian
100542228   洛扎县 lzx luozhaxian
100542229   加查县 jcx jiachaxian
100542231   隆子县 lzx longzixian
100542232   错那县 cnx cuoneixian
100542233   浪卡子县    lkzx    langkazixian
100542400   那曲地区    nqdq    neiqudiqu
100542421   那曲县 nqx neiquxian
100542422   嘉黎县 jlx jialixian
100542423   比如县 brx biruxian
100542424   聂荣县 nrx nierongxian
100542425   安多县 adx anduoxian
100542426   申扎县 szx shenzhaxian
100542427   索县  sx  suoxian
100542428   班戈县 bgx bangexian
100542429   巴青县 bqx baqingxian
100542430   尼玛县 nmx nimaxian
100542431   双湖县 shx shuanghuxian
100542500   阿里地区    aldq    alidiqu
100542521   普兰县 plx pulanxian
100542522   札达县 zdx zhadaxian
100542523   噶尔县 gex gaerxian
100542524   日土县 rtx rituxian
100542525   革吉县 gjx gejixian
100542526   改则县 gzx gaizexian
100542527   措勤县 cqx cuoqinxian
100542600   林芝地区    lzdq    linzhidiqu
100542621   林芝县 lzx linzhixian
100542622   工布江达县   gbjdx   gongbujiangdaxian
100542623   米林县 mlx milinxian
100542624   墨脱县 mtx motuoxian
100542625   波密县 bmx bomixian
100542626   察隅县 cyx chayuxian
100542627   朗县  lx  langxian
100610000   陕西省 sxs shanxisheng
100610100   西安市 xas xianshi
100610101   市辖区 sxq shixiaqu
100610102   新城区 xcq xinchengqu
100610103   碑林区 blq beilinqu
100610104   莲湖区 lhq lianhuqu
100610111   灞桥区 bqq baqiaoqu
100610112   未央区 wyq weiyangqu
100610113   雁塔区 ytq yantaqu
100610114   阎良区 ylq yanliangqu
100610115   临潼区 ltq lintongqu
100610116   长安区 zaq zhanganqu
100610122   蓝田县 ltx lantianxian
100610124   周至县 zzx zhouzhixian
100610125   户县  hx  huxian
100610126   高陵县 glx gaolingxian
100610200   铜川市 tcs tongchuanshi
100610201   市辖区 sxq shixiaqu
100610202   王益区 wyq wangyiqu
100610203   印台区 ytq yintaiqu
100610204   耀州区 yzq yaozhouqu
100610222   宜君县 yjx yijunxian
100610300   宝鸡市 bjs baojishi
100610301   市辖区 sxq shixiaqu
100610302   渭滨区 wbq weibinqu
100610303   金台区 jtq jintaiqu
100610304   陈仓区 ccq chencangqu
100610322   凤翔县 fxx fengxiangxian
100610323   岐山县 qsx qishanxian
100610324   扶风县 ffx fufengxian
100610326   眉县  mx  meixian
100610327   陇县  lx  longxian
100610328   千阳县 qyx qianyangxian
100610329   麟游县 lyx linyouxian
100610330   凤县  fx  fengxian
100610331   太白县 tbx taibaixian
100610400   咸阳市 xys xianyangshi
100610401   市辖区 sxq shixiaqu
100610402   秦都区 qdq qindouqu
100610403   杨陵区 ylq yanglingqu
100610404   渭城区 wcq weichengqu
100610422   三原县 syx sanyuanxian
100610423   泾阳县 jyx jingyangxian
100610424   乾县  qx  qianxian
100610425   礼泉县 lqx liquanxian
100610426   永寿县 ysx yongshouxian
100610427   彬县  bx  binxian
100610428   长武县 zwx zhangwuxian
100610429   旬邑县 xyx xunyixian
100610430   淳化县 chx chunhuaxian
100610431   武功县 wgx wugongxian
100610481   兴平市 xps xingpingshi
100610500   渭南市 wns weinanshi
100610501   市辖区 sxq shixiaqu
100610502   临渭区 lwq linweiqu
100610521   华县  hx  huaxian
100610522   潼关县 tgx tongguanxian
100610523   大荔县 dlx dalixian
100610524   合阳县 hyx heyangxian
100610525   澄城县 ccx chengchengxian
100610526   蒲城县 pcx puchengxian
100610527   白水县 bsx baishuixian
100610528   富平县 fpx fupingxian
100610581   韩城市 hcs hanchengshi
100610582   华阴市 hys huayinshi
100610600   延安市 yas yananshi
100610601   市辖区 sxq shixiaqu
100610602   宝塔区 btq baotaqu
100610621   延长县 yzx yanzhangxian
100610622   延川县 ycx yanchuanxian
100610623   子长县 zzx zizhangxian
100610624   安塞县 asx ansaixian
100610625   志丹县 zdx zhidanxian
100610626   吴起县 wqx wuqixian
100610627   甘泉县 gqx ganquanxian
100610628   富县  fx  fuxian
100610629   洛川县 lcx luochuanxian
100610630   宜川县 ycx yichuanxian
100610631   黄龙县 hlx huanglongxian
100610632   黄陵县 hlx huanglingxian
100610700   汉中市 hzs hanzhongshi
100610701   市辖区 sxq shixiaqu
100610702   汉台区 htq hantaiqu
100610721   南郑县 nzx nanzhengxian
100610722   城固县 cgx chengguxian
100610723   洋县  yx  yangxian
100610724   西乡县 xxx xixiangxian
100610725   勉县  mx  mianxian
100610726   宁强县 nqx ningqiangxian
100610727   略阳县 lyx lu:eyangxian
100610728   镇巴县 zbx zhenbaxian
100610729   留坝县 lbx liubaxian
100610730   佛坪县 fpx fopingxian
100610800   榆林市 yls yulinshi
100610801   市辖区 sxq shixiaqu
100610802   榆阳区 yyq yuyangqu
100610821   神木县 smx shenmuxian
100610822   府谷县 fgx fuguxian
100610823   横山县 hsx hengshanxian
100610824   靖边县 jbx jingbianxian
100610825   定边县 dbx dingbianxian
100610826   绥德县 sdx suidexian
100610827   米脂县 mzx mizhixian
100610828   佳县  jx  jiaxian
100610829   吴堡县 wbx wubaoxian
100610830   清涧县 qjx qingjianxian
100610831   子洲县 zzx zizhouxian
100610900   安康市 aks ankangshi
100610901   市辖区 sxq shixiaqu
100610902   汉滨区 hbq hanbinqu
100610921   汉阴县 hyx hanyinxian
100610922   石泉县 sqx shiquanxian
100610923   宁陕县 nsx ningshanxian
100610924   紫阳县 zyx ziyangxian
100610925   岚皋县 lgx langaoxian
100610926   平利县 plx pinglixian
100610927   镇坪县 zpx zhenpingxian
100610928   旬阳县 xyx xunyangxian
100610929   白河县 bhx baihexian
100611000   商洛市 sls shangluoshi
100611001   市辖区 sxq shixiaqu
100611002   商州区 szq shangzhouqu
100611021   洛南县 lnx luonanxian
100611022   丹凤县 dfx danfengxian
100611023   商南县 snx shangnanxian
100611024   山阳县 syx shanyangxian
100611025   镇安县 zax zhenanxian
100611026   柞水县 zsx zuoshuixian
100620000   甘肃省 gss gansusheng
100620100   兰州市 lzs lanzhoushi
100620101   市辖区 sxq shixiaqu
100620102   城关区 cgq chengguanqu
100620103   七里河区    qlhq    qilihequ
100620104   西固区 xgq xiguqu
100620105   安宁区 anq anningqu
100620111   红古区 hgq hongguqu
100620121   永登县 ydx yongdengxian
100620122   皋兰县 glx gaolanxian
100620123   榆中县 yzx yuzhongxian
100620200   嘉峪关市    jygs    jiayuguanshi
100620201   市辖区 sxq shixiaqu
100620300   金昌市 jcs jinchangshi
100620301   市辖区 sxq shixiaqu
100620302   金川区 jcq jinchuanqu
100620321   永昌县 ycx yongchangxian
100620400   白银市 bys baiyinshi
100620401   市辖区 sxq shixiaqu
100620402   白银区 byq baiyinqu
100620403   平川区 pcq pingchuanqu
100620421   靖远县 jyx jingyuanxian
100620422   会宁县 hnx huiningxian
100620423   景泰县 jtx jingtaixian
100620500   天水市 tss tianshuishi
100620501   市辖区 sxq shixiaqu
100620502   秦州区 qzq qinzhouqu
100620503   麦积区 mjq maijiqu
100620521   清水县 qsx qingshuixian
100620522   秦安县 qax qinanxian
100620523   甘谷县 ggx ganguxian
100620524   武山县 wsx wushanxian
100620525   张家川回族自治县    zjchzzzx    zhangjiachuanhuizuzizhixian
100620600   武威市 wws wuweishi
100620601   市辖区 sxq shixiaqu
100620602   凉州区 lzq liangzhouqu
100620621   民勤县 mqx minqinxian
100620622   古浪县 glx gulangxian
100620623   天祝藏族自治县 tzzzzzx tianzhuzangzuzizhixian
100620700   张掖市 zys zhangyeshi
100620701   市辖区 sxq shixiaqu
100620702   甘州区 gzq ganzhouqu
100620721   肃南裕固族自治县    snygzzzx    sunanyuguzuzizhixian
100620722   民乐县 mlx minlexian
100620723   临泽县 lzx linzexian
100620724   高台县 gtx gaotaixian
100620725   山丹县 sdx shandanxian
100620800   平凉市 pls pingliangshi
100620801   市辖区 sxq shixiaqu
100620802   崆峒区 ktq kongtongqu
100620821   泾川县 jcx jingchuanxian
100620822   灵台县 ltx lingtaixian
100620823   崇信县 cxx chongxinxian
100620824   华亭县 htx huatingxian
100620825   庄浪县 zlx zhuanglangxian
100620826   静宁县 jnx jingningxian
100620900   酒泉市 jqs jiuquanshi
100620901   市辖区 sxq shixiaqu
100620902   肃州区 szq suzhouqu
100620921   金塔县 jtx jintaxian
100620922   瓜州县 gzx guazhouxian
100620923   肃北蒙古族自治县    sbmgzzzx    subeimengguzuzizhixian
100620924   阿克塞哈萨克族自治县  akshskzzzx  akesaihasakezuzizhixian
100620981   玉门市 yms yumenshi
100620982   敦煌市 dhs dunhuangshi
100621000   庆阳市 qys qingyangshi
100621001   市辖区 sxq shixiaqu
100621002   西峰区 xfq xifengqu
100621021   庆城县 qcx qingchengxian
100621022   环县  hx  huanxian
100621023   华池县 hcx huachixian
100621024   合水县 hsx heshuixian
100621025   正宁县 znx zhengningxian
100621026   宁县  nx  ningxian
100621027   镇原县 zyx zhenyuanxian
100621100   定西市 dxs dingxishi
100621101   市辖区 sxq shixiaqu
100621102   安定区 adq andingqu
100621121   通渭县 twx tongweixian
100621122   陇西县 lxx longxixian
100621123   渭源县 wyx weiyuanxian
100621124   临洮县 ltx lintaoxian
100621125   漳县  zx  zhangxian
100621126   岷县  mx  minxian
100621200   陇南市 lns longnanshi
100621201   市辖区 sxq shixiaqu
100621202   武都区 wdq wudouqu
100621221   成县  cx  chengxian
100621222   文县  wx  wenxian
100621223   宕昌县 dcx dangchangxian
100621224   康县  kx  kangxian
100621225   西和县 xhx xihexian
100621226   礼县  lx  lixian
100621227   徽县  hx  huixian
100621228   两当县 ldx liangdangxian
100622900   临夏回族自治州 lxhzzzz linxiahuizuzizhizhou
100622901   临夏市 lxs linxiashi
100622921   临夏县 lxx linxiaxian
100622922   康乐县 klx kanglexian
100622923   永靖县 yjx yongjingxian
100622924   广河县 ghx guanghexian
100622925   和政县 hzx hezhengxian
100622926   东乡族自治县  dxzzzx  dongxiangzuzizhixian
100623000   甘南藏族自治州 gnzzzzz gannanzangzuzizhizhou
100623001   合作市 hzs hezuoshi
100623021   临潭县 ltx lintanxian
100623022   卓尼县 znx zhuonixian
100623023   舟曲县 zqx zhouquxian
100623024   迭部县 dbx diebuxian
100623025   玛曲县 mqx maquxian
100623026   碌曲县 lqx liuquxian
100623027   夏河县 xhx xiahexian
100630000   青海省 qhs qinghaisheng
100630100   西宁市 xns xiningshi
100630101   市辖区 sxq shixiaqu
100630102   城东区 cdq chengdongqu
100630103   城中区 czq chengzhongqu
100630104   城西区 cxq chengxiqu
100630105   城北区 cbq chengbeiqu
100630121   大通回族土族自治县   dthztzzzx   datonghuizutuzuzizhixian
100630122   湟中县 hzx huangzhongxian
100630123   湟源县 hyx huangyuanxian
100630200   海东市 hds haidongshi
100630202   乐都区 ldq ledouqu
100630221   平安县 pax pinganxian
100630222   民和回族土族自治县   mhhztzzzx   minhehuizutuzuzizhixian
100630223   互助土族自治县 hztzzzx huzhutuzuzizhixian
100630224   化隆回族自治县 hlhzzzx hualonghuizuzizhixian
100630225   循化撒拉族自治县    xhslzzzx    xunhuasalazuzizhixian
100632200   海北藏族自治州 hbzzzzz haibeizangzuzizhizhou
100632221   门源回族自治县 myhzzzx menyuanhuizuzizhixian
100632222   祁连县 qlx qilianxian
100632223   海晏县 hyx haiyanxian
100632224   刚察县 gcx gangchaxian
100632300   黄南藏族自治州 hnzzzzz huangnanzangzuzizhizhou
100632321   同仁县 trx tongrenxian
100632322   尖扎县 jzx jianzhaxian
100632323   泽库县 zkx zekuxian
100632324   河南蒙古族自治县    hnmgzzzx    henanmengguzuzizhixian
100632500   海南藏族自治州 hnzzzzz hainanzangzuzizhizhou
100632521   共和县 ghx gonghexian
100632522   同德县 tdx tongdexian
100632523   贵德县 gdx guidexian
100632524   兴海县 xhx xinghaixian
100632525   贵南县 gnx guinanxian
100632600   果洛藏族自治州 glzzzzz guoluozangzuzizhizhou
100632621   玛沁县 mqx maqinxian
100632622   班玛县 bmx banmaxian
100632623   甘德县 gdx gandexian
100632624   达日县 drx darixian
100632625   久治县 jzx jiuzhixian
100632626   玛多县 mdx maduoxian
100632700   玉树藏族自治州 yszzzzz yushuzangzuzizhizhou
100632701   玉树市 yss yushushi
100632722   杂多县 zdx zaduoxian
100632723   称多县 cdx chengduoxian
100632724   治多县 zdx zhiduoxian
100632725   囊谦县 nqx nangqianxian
100632726   曲麻莱县    qmlx    qumalaixian
100632800   海西蒙古族藏族自治州  hxmgzzzzzz  haiximengguzuzangzuzizhizhou
100632801   格尔木市    gems    geermushi
100632802   德令哈市    dlhs    delinghashi
100632821   乌兰县 wlx wulanxian
100632822   都兰县 dlx doulanxian
100632823   天峻县 tjx tianjunxian
100640000   宁夏回族自治区 nxhzzzq ningxiahuizuzizhiqu
100640100   银川市 ycs yinchuanshi
100640101   市辖区 sxq shixiaqu
100640104   兴庆区 xqq xingqingqu
100640105   西夏区 xxq xixiaqu
100640106   金凤区 jfq jinfengqu
100640121   永宁县 ynx yongningxian
100640122   贺兰县 hlx helanxian
100640181   灵武市 lws lingwushi
100640200   石嘴山市    szss    shizuishanshi
100640201   市辖区 sxq shixiaqu
100640202   大武口区    dwkq    dawukouqu
100640205   惠农区 hnq huinongqu
100640221   平罗县 plx pingluoxian
100640300   吴忠市 wzs wuzhongshi
100640301   市辖区 sxq shixiaqu
100640302   利通区 ltq litongqu
100640303   红寺堡区    hsbq    hongsibaoqu
100640323   盐池县 ycx yanchixian
100640324   同心县 txx tongxinxian
100640381   青铜峡市    qtxs    qingtongxiashi
100640400   固原市 gys guyuanshi
100640401   市辖区 sxq shixiaqu
100640402   原州区 yzq yuanzhouqu
100640422   西吉县 xjx xijixian
100640423   隆德县 ldx longdexian
100640424   泾源县 jyx jingyuanxian
100640425   彭阳县 pyx pengyangxian
100640500   中卫市 zws zhongweishi
100640501   市辖区 sxq shixiaqu
100640502   沙坡头区    sptq    shapotouqu
100640521   中宁县 znx zhongningxian
100640522   海原县 hyx haiyuanxian
100650000   新疆维吾尔自治区    xjwwezzq    xinjiangweiwuerzizhiqu
100650100   乌鲁木齐市   wlmqs   wulumuqishi
100650101   市辖区 sxq shixiaqu
100650102   天山区 tsq tianshanqu
100650103   沙依巴克区   sybkq   shayibakequ
100650104   新市区 xsq xinshiqu
100650105   水磨沟区    smgq    shuimogouqu
100650106   头屯河区    tthq    toutunhequ
100650107   达坂城区    dbcq    dabanchengqu
100650109   米东区 mdq midongqu
100650121   乌鲁木齐县   wlmqx   wulumuqixian
100650200   克拉玛依市   klmys   kelamayishi
100650201   市辖区 sxq shixiaqu
100650202   独山子区    dszq    dushanziqu
100650203   克拉玛依区   klmyq   kelamayiqu
100650204   白碱滩区    bjtq    baijiantanqu
100650205   乌尔禾区    wehq    wuerhequ
100652100   吐鲁番地区   tlfdq   tulufandiqu
100652101   吐鲁番市    tlfs    tulufanshi
100652122   鄯善县 ssx shanshanxian
100652123   托克逊县    tkxx    tuokexunxian
100652200   哈密地区    hmdq    hamidiqu
100652201   哈密市 hms hamishi
100652222   巴里坤哈萨克自治县   blkhskzzx   balikunhasakezizhixian
100652223   伊吾县 ywx yiwuxian
100652300   昌吉回族自治州 cjhzzzz changjihuizuzizhizhou
100652301   昌吉市 cjs changjishi
100652302   阜康市 fks fukangshi
100652323   呼图壁县    htbx    hutubixian
100652324   玛纳斯县    mnsx    manasixian
100652325   奇台县 qtx qitaixian
100652327   吉木萨尔县   jmsex   jimusaerxian
100652328   木垒哈萨克自治县    mlhskzzx    muleihasakezizhixian
100652700   博尔塔拉蒙古自治州   betlmgzzz   boertalamengguzizhizhou
100652701   博乐市 bls boleshi
100652702   阿拉山口市   alsks   alashankoushi
100652722   精河县 jhx jinghexian
100652723   温泉县 wqx wenquanxian
100652800   巴音郭楞蒙古自治州   byglmgzzz   bayinguolengmengguzizhizhou
100652801   库尔勒市    kels    kuerleshi
100652822   轮台县 ltx luntaixian
100652823   尉犁县 wlx weilixian
100652824   若羌县 rqx ruoqiangxian
100652825   且末县 qmx qiemoxian
100652826   焉耆回族自治县 yqhzzzx yanqihuizuzizhixian
100652827   和静县 hjx hejingxian
100652828   和硕县 hsx heshuoxian
100652829   博湖县 bhx bohuxian
100652900   阿克苏地区   aksdq   akesudiqu
100652901   阿克苏市    akss    akesushi
100652922   温宿县 wsx wensuxian
100652923   库车县 kcx kuchexian
100652924   沙雅县 syx shayaxian
100652925   新和县 xhx xinhexian
100652926   拜城县 bcx baichengxian
100652927   乌什县 wsx wushenxian
100652928   阿瓦提县    awtx    awatixian
100652929   柯坪县 kpx kepingxian
100653000   克孜勒苏柯尔克孜自治州 kzlskekzzzz kezilesukeerkezizizhizhou
100653001   阿图什市    atss    atushenshi
100653022   阿克陶县    aktx    aketaoxian
100653023   阿合奇县    ahqx    aheqixian
100653024   乌恰县 wqx wuqiaxian
100653100   喀什地区    ksdq    kashendiqu
100653101   喀什市 kss kashenshi
100653121   疏附县 sfx shufuxian
100653122   疏勒县 slx shulexian
100653123   英吉沙县    yjsx    yingjishaxian
100653124   泽普县 zpx zepuxian
100653125   莎车县 scx shachexian
100653126   叶城县 ycx yechengxian
100653127   麦盖提县    mgtx    maigaitixian
100653128   岳普湖县    yphx    yuepuhuxian
100653129   伽师县 jsx jiashixian
100653130   巴楚县 bcx bachuxian
100653131   塔什库尔干塔吉克自治县 tskegtjkzzx tashenkuergantajikezizhixian
100653200   和田地区    htdq    hetiandiqu
100653201   和田市 hts hetianshi
100653221   和田县 htx hetianxian
100653222   墨玉县 myx moyuxian
100653223   皮山县 psx pishanxian
100653224   洛浦县 lpx luopuxian
100653225   策勒县 clx celexian
100653226   于田县 ytx yutianxian
100653227   民丰县 mfx minfengxian
100654000   伊犁哈萨克自治州    ylhskzzz    yilihasakezizhizhou
100654002   伊宁市 yns yiningshi
100654003   奎屯市 kts kuitunshi
100654021   伊宁县 ynx yiningxian
100654022   察布查尔锡伯自治县   cbcexbzzx   chabuchaerxibozizhixian
100654023   霍城县 hcx huochengxian
100654024   巩留县 glx gongliuxian
100654025   新源县 xyx xinyuanxian
100654026   昭苏县 zsx zhaosuxian
100654027   特克斯县    tksx    tekesixian
100654028   尼勒克县    nlkx    nilekexian
100654200   塔城地区    tcdq    tachengdiqu
100654201   塔城市 tcs tachengshi
100654202   乌苏市 wss wusushi
100654221   额敏县 emx eminxian
100654223   沙湾县 swx shawanxian
100654224   托里县 tlx tuolixian
100654225   裕民县 ymx yuminxian
100654226   和布克赛尔蒙古自治县  hbksemgzzx  hebukesaiermengguzizhixian
100654300   阿勒泰地区   altdq   aletaidiqu
100654301   阿勒泰市    alts    aletaishi
100654321   布尔津县    bejx    buerjinxian
100654322   富蕴县 fyx fuyunxian
100654323   福海县 fhx fuhaixian
100654324   哈巴河县    hbhx    habahexian
100654325   青河县 qhx qinghexian
100654326   吉木乃县    jmnx    jimunaixian
100659000   自治区直辖县级行政区划 zzqzxxjxzqh zizhiquzhixiaxianjixingzhengquhua
100659001   石河子市    shzs    shihezishi
100659002   阿拉尔市    ales    alaershi
100659003   图木舒克市   tmsks   tumushukeshi
100659004   五家渠市    wjqs    wujiaqushi
100710000   台湾省 tws taiwansheng
100710100   台北市 tbs 
100710200   高雄市 gxs 
100710300   基隆市 jls 
100710400   台中市 tzs 
100710500   台南市 tns 
100710600   新竹市 xzs 
100710700   嘉义市 jys 
100710800   台北县 tbx 
100710900   宜兰县 ylx 
100711000   桃园县 tyx 
100711100   新竹县 xzx 
100711200   苗栗县 mlx 
100711300   台中县 tzx 
100711400   彰化县 zhx 
100711500   南投县 ytx 
100711600   云林县 ylx 
100711700   嘉义县 jyx 
100711800   台南县 tnx 
100711900   高雄县 gxx 
100712000   屏东县 bdx 
100712100   澎湖县 phx 
100712200   台东县 tdx 
100712300   花莲县 hlx 
100810000   香港特别行政区 xgtbxzq xianggangtebiexingzhengqu
100810100   中西区 zxq 
100810200   东区  dq  
100810300   九龙城区    jlcq    
100810400   观塘区 gtq 
100810500   南区  nq  
100810600   深水埗区    ssbq    
100810700   黄大仙区    hdxq    
100810800   湾仔区 wzq 
100810900   油尖旺区    yjwq    
100811000   离岛区 ldq 
100811100   葵青区 kqq 
100811200   北区  bq  
100811300   西贡区 xgq 
100811400   沙田区 stq 
100811500   屯门区 tmq 
100811600   大埔区 dbq 
100811700   荃湾区 qwq 
100811800   元朗区 ylq 
100820000   澳门特别行政区 amtbxzq aomentebiexingzhengqu
100820100   花地玛堂区   hdmtq   
100820200   圣安多尼堂区  sadntq  
100820300   大堂区 dtq 
100820400   望德堂区    wdtq    
100820500   风顺堂区    fstq    
100820600   氹仔  dz  
100820700   路环  lh  
101000000   阿尔巴尼亚   aebny   
101110000   爱尔巴桑    aebs    
101120000   迪勃拉 dbl 
101130000   地拉那 dln 
101140000   都拉斯 dls 
101150000   发罗拉 fll 
101160000   费里  fl  
101170000   吉诺卡斯特   jnkst   
101180000   科尔察 kec 
101190000   库克斯 kks 
101200000   莱什  ls  
101210000   培拉特 plt 
101220000   斯库台 skt 
102000000   阿尔及利亚   aejly   
102110000   阿德拉尔    adle    
102120000   阿尔及尔    aeje    
102130000   艾因·德夫拉  ay·dfl  
102140000   艾因·蒂姆尚特 ay·dmst 
102150000   安纳巴 anb 
102160000   奥兰  al  
102170000   巴特纳 btn 
102180000   贝贾亚 bjy 
102190000   贝沙尔 bse 
102200000   贝伊德 byd 
102210000   比斯克拉    bskl    
102220000   布尔吉·布阿雷里吉   bej·ballj   
102230000   布利达 bld 
102240000   布迈德斯    bmds    
102250000   布依拉 byl 
102260000   蒂巴扎 dbz 
102270000   蒂斯姆西勒特  dsmxlt  
102280000   盖尔达耶    gedy    
102290000   盖尔马 gem 
102300000   罕西拉 hxl 
102310000   赫利赞 hlz 
102320000   吉杰尔 jje 
102330000   杰勒法 jlf 
102340000   君士坦丁    jstd    
102350000   拉格瓦特    lgwt    
102360000   马斯卡拉    mskl    
102370000   麦迪亚 mdy 
102380000   密拉  ml  
102390000   莫斯塔加纳姆  mstjnm  
102400000   姆西拉 mxl 
102410000   纳阿马 nam 
102420000   塞蒂夫 sdf 
102430000   赛伊达 syd 
102440000   斯基克达    sjkd    
102450000   苏克·阿赫拉斯 sk·ahls 
102460000   塔里夫 tlf 
102470000   塔曼拉塞特   tmlst   
102480000   特贝萨 tbs 
102490000   特莱姆森    tlms    
102500000   提济乌祖    tjwz    
102510000   提亚雷特    tylt    
102520000   廷杜夫 tdf 
102530000   瓦德  wd  
102540000   瓦尔格拉    wegl    
102550000   乌姆布阿基   wmbaj   
102560000   西迪贝勒阿贝斯 xdblabs 
102570000   谢里夫 xlf 
102580000   伊利齐 ylq 
103000000   阿富汗 afh 
103110000   赫拉特 hlt 
103120000   喀布尔 kbe 
103130000   坎大哈 kdh 
103140000   马扎里沙里夫  mzlslf  
104000000   阿根廷 agt 
104110000   巴拉那 bln 
104120000   别德马 bdm 
104130000   波萨达斯    bsds    
104140000   布兰卡港    blkg    
104150000   布宜诺斯艾利斯 bynsals 
104160000   福莫萨 fms 
104170000   胡胡伊 hhy 
104180000   卡塔马卡    ktmk    
104190000   科尔多瓦    kedw    
104200000   科连特斯    klts    
104210000   克劳斯城    klsc    
104220000   肯考迪娅    kkdy    
104230000   拉里奥哈    llah    
104240000   拉普拉塔    lplt    
104250000   雷西斯滕匹亚  lxstpy  
104260000   里奥加耶戈斯  lajygs  
104270000   里奥夸尔托   laket   
104280000   里瓦达维亚海军准将城  lwdwyhjzjc  
104290000   罗萨里奥    lsla    
104300000   罗森  ls  
104310000   马德普拉塔   mdplt   
104320000   门多萨 mds 
104330000   内乌肯 nwk 
104340000   萨尔塔 set 
104350000   圣地亚哥-德尔埃斯特罗 sdyg-deastl 
104360000   圣菲  sf  
104370000   圣胡安 sha 
104380000   圣拉斐尔    slfe    
104390000   圣路易斯    slys    
104400000   圣罗莎 sls 
104410000   圣米格尔-德图库曼   smge-dtkm   
104420000   圣尼古拉斯   sngls   
104430000   特雷利乌    tllw    
104440000   乌斯怀亚    wshy    
105000000   阿拉伯联合酋长国    alblhqzg    
105110000   阿布扎比    abzb    
105120000   艾因  ay  
105130000   迪拜  db  
105140000   沙迦  sj  
106000000   阿鲁巴 alb 
107000000   阿曼  am  
107110000   巴提奈地区   btndq   
107120000   达希莱地区   dxldq   
107130000   东部地区    dbdq    
107140000   马斯喀特省   mskts   
107150000   穆桑达姆省   msdms   
107160000   内地地区    nddq    
107170000   中部地区    zbdq    
107180000   佐法尔省    zfes    
108000000   阿塞拜疆    asbj    
108110000   阿布歇隆    abxl    
108120000   哈奇马斯    hqms    
108130000   卡尔巴卡尔   kebke   
108140000   卡扎赫 kzh 
108150000   连科兰 lkl 
108160000   密尔-卡拉巴赫 me-klbh 
108170000   穆甘-萨连   mg-sl   
108180000   纳戈尔诺－卡拉巴赫   ngen－klbh   
108190000   纳希切万    nxqw    
108200000   普利亚拉克斯  plylks  
108210000   舍基  sj  
108220000   苏姆盖特    smgt    
108230000   锡尔万 xew 
108240000   占贾  zj  
109000000   阿森松岛    assd    
110000000   埃及  aj  
110110000   阿斯旺 asw 
110120000   古尔代盖    gedg    
110130000   开罗  kl  
110140000   苏布拉开马   sblkm   
110150000   亚历山大    ylsd    
111000000   埃塞俄比亚   aseby   
111110000   阿法尔 afe 
111120000   阿姆哈拉    amhl    
111130000   奥罗米亚    almy    
111140000   宾香古尔    bxge    
111150000   德雷达瓦    dldw    
111160000   甘贝拉各族   gblgz   
111170000   哈勒里民族   hllmz   
111180000   南方各族    nfgz    
111190000   索马里 sml 
111200000   提格雷 tgl 
111210000   亚的斯亚贝巴  ydsybb  
112000000   爱尔兰 ael 
112110000   奥法利 afl 
112120000   蒂珀雷里    dpll    
112130000   都柏林 dbl 
112140000   多内加尔    dnje    
112150000   戈尔韦 gew 
112160000   基尔代尔    jede    
112170000   基尔肯尼    jekn    
112180000   卡范  kf  
112190000   卡洛  kl  
112200000   凯里  kl  
112210000   科克  kk  
112220000   克莱尔 kle 
112230000   朗福德 lfd 
112240000   劳斯  ls  
112250000   崂斯  ls  
112260000   利默里克    lmlk    
112270000   利特里姆    ltlm    
112280000   罗斯康芒    lskm    
112290000   梅奥  ma  
112300000   米斯  ms  
112310000   莫内根 mng 
112320000   斯莱戈 slg 
112330000   威克洛 wkl 
112340000   韦克斯福德   wksfd   
112350000   沃特福德    wtfd    
112360000   西米斯 xms 
113000000   爱沙尼亚    asny    
113110000   贝尔瓦 bew 
113120000   哈留  hl  
113130000   拉普拉 lpl 
113140000   里亚内 lyn 
113150000   帕尔努 pen 
113160000   萨雷  sl  
113170000   塔尔图 tet 
113180000   瓦尔加 wej 
113190000   维良地 wld 
113200000   维鲁  wl  
113210000   沃鲁  wl  
113220000   希尤  xy  
113230000   耶尔韦 yew 
113240000   耶盖瓦 ygw 
113250000   依达－维鲁   yd－wl   
114000000   安道尔 ade 
114110000   安道尔城    adec    
114120000   奥尔迪诺    aedn    
114130000   恩坎普 ekp 
114140000   卡尼略 knl 
114150000   莱塞斯卡尔德－恩戈尔达 lssked－eged 
114160000   马萨纳 msn 
114170000   圣胡利娅－德洛里亚   shly－dlly   
115000000   安哥拉 agl 
115110000   北宽扎 bkz 
115120000   北隆达 bld 
115130000   本戈  bg  
115140000   本格拉 bgl 
115150000   比耶  by  
115160000   卡宾达 kbd 
115170000   库内内 knn 
115180000   宽多库邦戈   kdkbg   
115190000   罗安达 lad 
115200000   马兰热 mlr 
115210000   莫希科 mxk 
115220000   纳米贝 nmb 
115230000   南宽扎 nkz 
115240000   南隆达 nld 
115250000   万博  wb  
115260000   威拉  wl  
115270000   威热  wr  
115280000   扎伊尔 zye 
116000000   安圭拉 agl 
117000000   安提瓜岛和巴布达    atgdhbbd    
118000000   澳大利亚    adly    
118110000   北部地区    bbdq    
118110100   北帕默斯顿   bpmsd   
118110200   达尔文 dew 
118120000   堪培拉 kpl 
118120100   堪培拉 kpl 
118130000   昆士兰 ksl 
118130100   布里斯班    blsb    
118130200   黄金海岸    hjha    
118130300   凯恩斯 kes 
118130400   日光海岸    rgha    
118130500   汤斯维尔    tswe    
118130600   图文巴 twb 
118140000   南澳大利亚   nadly   
118140100   阿德莱德    adld    
118140200   奥古斯塔港   agstg   
118140300   甘比亚山    gbys    
118140400   怀阿拉 hal 
118140500   林肯港 lkg 
118140600   默里布里奇   mlblq   
118140700   皮里港 plg 
118140800   维克托港    wktg    
118150000   塔斯马尼亚   tsmny   
118150100   伯尼港 bng 
118150200   德文波特    dwbt    
118150300   霍巴特 hbt 
118150400   朗塞斯顿    lssd    
118160000   维多利亚    wdly    
118160100   吉朗  jl  
118160200   墨尔本 meb 
118170000   西澳大利亚   xadly   
118170100   奥尔巴尼    aebn    
118170200   班伯里 bbl 
118170300   弗里曼特尔港  flmteg  
118170400   杰拉尔顿    jled    
118170500   卡尔古利    kegl    
118170600   曼哲拉 mzl 
118170700   珀斯  ps  
118180000   新南威尔士   xnwes   
118180100   纽卡斯尔    nkse    
118180200   伍伦贡 wlg 
118180300   悉尼  xn  
119000000   奥地利 adl 
119110000   布尔根兰    begl    
119120000   蒂罗尔 dle 
119130000   福拉尔贝格   flebg   
119140000   克恩顿 ked 
119150000   萨尔茨堡    secb    
119160000   上奥地利    sadl    
119170000   施蒂利亚    sdly    
119180000   维也纳 wyn 
119190000   下奥地利    xadl    
120000000   奥兰群岛    alqd    
121000000   巴巴多斯岛   bbdsd   
122000000   巴布亚新几内亚 bbyxjny 
122110000   北部  bb  
122120000   布干维尔    bgwe    
122130000   东部高地    dbgd    
122140000   东塞皮克    dspk    
122150000   东新不列颠   dxbld   
122160000   恩加  ej  
122170000   海湾  hw  
122180000   马当  md  
122190000   马努斯 mns 
122200000   米尔恩湾    meew    
122210000   莫尔兹比港   mezbg   
122220000   莫罗贝 mlb 
122230000   南部高地    nbgd    
122240000   钦布  qb  
122250000   桑道恩 sde 
122260000   西部  xb  
122270000   西部高地    xbgd    
122280000   西新不列颠   xxbld   
122290000   新爱尔兰    xael    
123000000   巴哈马 bhm 
124000000   巴基斯坦    bjst    
124110000   白沙瓦 bsw 
124120000   费萨拉巴德   fslbd   
124130000   故吉软瓦拉   gjrwl   
124140000   海德拉巴    hdlb    
124150000   卡拉奇 klq 
124160000   拉合尔 lhe 
124170000   拉瓦尔品第   lwepd   
124180000   木尔坦 met 
124190000   伊斯兰堡    yslb    
125000000   巴拉圭 blg 
125110000   阿曼拜 amb 
125120000   阿耶斯总统省  ayszts  
125130000   巴拉瓜里    blgl    
125140000   博克龙 bkl 
125150000   瓜伊拉 gyl 
125160000   卡瓜苏 kgs 
125170000   卡嫩迪尤    kndy    
125180000   卡萨帕 ksp 
125190000   康塞普西翁   kspxw   
125200000   科迪勒拉    kdll    
125210000   米西奥内斯   mxans   
125220000   涅恩布库    nebk    
125230000   上巴拉圭    sblg    
125240000   上巴拉那    sbln    
125250000   圣佩德罗    spdl    
125260000   亚松森特别区  ysstbq  
125270000   伊塔普亚    ytpy    
125280000   中央  zy  
126000000   巴勒斯坦    blst    
126110000   加沙地带    jsdd    
126120000   西岸  xa  
127000000   巴林  bl  
127110000   北部  bb  
127120000   哈德  hd  
127130000   哈马德 hmd 
127140000   里法  lf  
127150000   麦纳麦 mnm 
127160000   穆哈拉格    mhlg    
127170000   西部  xb  
127180000   伊萨城 ysc 
127190000   中部  zb  
128000000   巴拿马 bnm 
129000000   巴西  bx  
129110000   阿克里 akl 
129120000   阿拉戈斯    algs    
129130000   阿马帕 amp 
129140000   巴拉那 bln 
129150000   巴西利亚    bxly    
129160000   巴伊亚 byy 
129170000   北里奥格兰德  blagld  
129180000   伯南布哥    bnbg    
129190000   戈亚斯 gys 
129200000   朗多尼亚    ldny    
129210000   里约热内卢   lyrnl   
129220000   罗赖马 llm 
129230000   马拉尼昂    mlna    
129240000   马托格罗索   mtgls   
129250000   米纳斯吉拉斯  mnsjls  
129260000   南里奥格兰德  nlagld  
129270000   南马托格罗索  nmtgls  
129280000   帕拉  pl  
129290000   帕拉伊巴    plyb    
129300000   皮奥伊 pay 
129310000   塞阿拉 sal 
129320000   塞尔希培    sexp    
129330000   圣埃斯皮里图  sasplt  
129340000   圣保罗 sbl 
129350000   圣卡塔琳娜   sktln   
129360000   托坎廷斯    tkts    
129370000   亚马孙 yms 
130000000   白俄罗斯    bels    
130110000   布列斯特    blst    
130120000   戈梅利 gml 
130130000   格罗德诺    gldn    
130140000   明斯克市    msks    
130150000   莫吉廖夫    mjlf    
130160000   维捷布斯克   wjbsk   
131000000   百慕大 bmd 
132000000   保加利亚    bjly    
132110000   布尔加斯    bejs    
132120000   卡斯科伏    kskf    
132130000   鲁塞  ls  
132140000   洛维奇 lwq 
132150000   蒙塔纳 mtn 
132160000   普罗夫迪夫   plfdf   
132170000   索非亚 sfy 
132180000   索非亚市    sfys    
132190000   瓦尔纳 wen 
133000000   北马里亚纳群岛 bmlynqd 
134000000   贝宁  bn  
134110000   阿黎博里    albl    
134120000   阿塔科拉    atkl    
134130000   滨海  bh  
134140000   波希康市    bxks    
134150000   博尔古 beg 
134160000   大西洋 dxy 
134170000   高原  gy  
134180000   库福  kf  
134190000   莫诺  mn  
134200000   丘陵  ql  
134210000   韦梅  wm  
134220000   峡谷  xg  
134230000   祖   z   
135000000   比利时 bls 
135110000   埃诺  an  
135120000   安特卫普    atwp    
135130000   布拉班特-瓦隆 blbt-wl 
135140000   布鲁塞尔    blse    
135150000   东佛兰德    dfld    
135160000   佛兰芒-布拉班特    flm-blbt    
135170000   列日  lr  
135180000   林堡  lb  
135190000   卢森堡 lsb 
135200000   那慕尔 nme 
135210000   西佛兰德    xfld    
136000000   冰岛  bd  
137000000   波多黎各    bdlg    
138000000   波兰  bl  
138110000   埃尔布隆格   aeblg   
138120000   奥尔什丁    aesd    
138130000   奥斯特罗文卡  astlwk  
138140000   比得哥什    bdgs    
138150000   彼得库夫    bdkf    
138160000   比托姆 btm 
138170000   比亚瓦波德拉斯卡    bywbdlsk    
138180000   比亚维斯托克  bywstk  
138190000   波莱  bl  
138200000   波兹南 bzn 
138210000   达布罗瓦戈尼察 dblwgnc 
138220000   大波兰地区戈茹夫    dbldqgrf    
138230000   弗罗茨瓦夫   flcwf   
138240000   弗沃茨瓦韦克  fwcwwk  
138250000   格但斯克    gdsk    
138260000   格丁尼亚    gdny    
138270000   格利维采    glwc    
138280000   格鲁琼兹    glqz    
138290000   海乌姆 hwm 
138300000   华沙  hs  
138310000   霍茹夫 hrf 
138320000   卡利什 kls 
138330000   卡托维兹    ktwz    
138340000   凯尔采 kec 
138350000   科宁  kn  
138360000   科沙林 ksl 
138370000   克拉科夫    klkf    
138380000   克罗斯诺    klsn    
138390000   拉多姆 ldm 
138400000   莱格尼察    lgnc    
138410000   莱什诺 lsn 
138420000   卢布林 lbl 
138430000   鲁达  ld  
138440000   罗兹  lz  
138450000   绿山城 lsc 
138460000   米什洛维采   mslwc   
138470000   皮瓦  pw  
138480000   普热梅希尔   prmxe   
138490000   普沃茨克    pwck    
138500000   切哈努夫    qhnf    
138510000   热舒夫 rsf 
138520000   什切青 sqq 
138530000   斯凯尔涅维采  skenwc  
138540000   斯武普斯克   swpsk   
138550000   苏瓦乌基    swwj    
138560000   索波特 sbt 
138570000   索斯诺维茨   ssnwc   
138580000   塔尔努夫    tenf    
138590000   塔尔诺布热格  tenbrg  
138600000   特切  tq  
138610000   托伦  tl  
138620000   瓦乌布日赫   wwbrh   
138630000   沃姆扎 wmz 
138640000   希米亚诺维采  xmynwc  
138650000   希维诺乌伊希切 xwnwyxq 
138660000   希维托赫洛维采 xwthlwc 
138670000   谢德尔采    xdec    
138680000   谢拉兹 xlz 
138690000   新松奇 xsq 
138700000   雅沃兹诺    ywzn    
138710000   耶莱尼亚古拉  ylnygl  
138720000   扎布热 zbr 
138730000   扎莫希奇    zmxq    
139000000   玻利维亚    blwy    
139110000   奥尔托 aet 
139120000   奥鲁罗 all 
139130000   贝尼  bn  
139140000   波多西 bdx 
139150000   基拉科洛    jlkl    
139160000   科恰班巴    kqbb    
139170000   拉巴斯 lbs 
139180000   潘多  pd  
139190000   丘基萨卡    qjsk    
139200000   萨卡巴 skb 
139210000   圣克鲁斯    skls    
139220000   塔里哈 tlh 
140000000   波斯尼亚和黑塞哥维那  bsnyhhsgwn  
140110000   波萨维纳    bswn    
140120000   波斯尼亚－波德里涅   bsny－bdln   
140130000   多米斯拉夫格勒 dmslfgl 
140140000   黑塞哥维那－涅雷特瓦  hsgwn－nltw  
140150000   萨拉热窝    slrw    
140160000   图兹拉－波德里涅    tzl－bdln    
140170000   乌纳－萨纳   wn－sn   
140180000   西波斯尼亚   xbsny   
140190000   西黑塞哥维那  xhsgwn  
140200000   泽尼察－多博伊 znc－dby 
140210000   中波斯尼亚   zbsny   
141000000   博茨瓦纳    bcwn    
142000000   伯利兹 blz 
142110000   伯利兹 blz 
142120000   橘园  jy  
142130000   卡约  ky  
142140000   科罗萨尔    klse    
142150000   斯坦港 stg 
142160000   托莱多 tld 
143000000   不丹  bd  
144000000   布基纳法索   bjnfs   
144110000   巴雷  bl  
144120000   巴姆  bm  
144130000   巴瓦  bw  
144140000   巴泽加 bzj 
144150000   波尼  bn  
144160000   布尔古 beg 
144170000   布尔基恩德   bejed   
144180000   布古里巴    bglb    
144190000   冈祖尔古    gzeg    
144200000   古尔马 gem 
144210000   济罗  jl  
144220000   卡焦戈 kjg 
144230000   凯内杜古    kndg    
144240000   科蒙加里    kmjl    
144250000   科莫埃 kma 
144260000   孔皮恩加    kpej    
144270000   孔西  kx  
144280000   库尔佩罗戈   keplg   
144290000   库尔维奥戈   kewag   
144300000   库里滕加    kltj    
144310000   雷拉巴 llb 
144320000   罗卢姆 llm 
144330000   穆翁  mw  
144340000   纳门滕加    nmtj    
144350000   纳乌里 nwl 
144360000   纳亚拉 nyl 
144370000   尼亚尼亚    nyny    
144380000   努姆比埃尔   nmbae   
144390000   帕索雷 psl 
144400000   塞诺  sn  
144410000   桑吉  sj  
144420000   桑马滕加    smtj    
144430000   苏鲁  sl  
144440000   苏姆  sm  
144450000   塔波阿 tba 
144460000   图伊  ty  
144470000   乌埃  wa  
144480000   乌布里滕加   wbltj   
144490000   乌达兰 wdl 
144500000   锡西里 xxl 
144510000   亚加  yj  
144520000   亚滕加 ytj 
144530000   伊奥巴 yab 
144540000   宗德韦奥戈   zdwag   
144550000   宗多马 zdm 
145000000   布隆迪 bld 
145110000   布班扎 bbz 
145120000   布鲁里 bll 
145130000   布琼布拉城市  bqblcs  
145140000   布琼布拉乡村  bqblxc  
145150000   恩戈齐 egq 
145160000   基龙多 jld 
145170000   基特加 jtj 
145180000   卡鲁济 klj 
145190000   卡扬扎 kyz 
145200000   坎库佐 kkz 
145210000   鲁塔纳 ltn 
145220000   鲁伊吉 lyj 
145230000   马坎巴 mkb 
145240000   穆拉姆维亚   mlmwy   
145250000   穆瓦洛 mwl 
145260000   穆因加 myj 
145270000   锡比托凯    xbtk    
146000000   布韦岛 bwd 
147000000   朝鲜  cx  
147110000   海州  hz  
147120000   惠山  hs  
147130000   江界  jj  
147140000   开城  kc  
147150000   罗先  lx  
147160000   南浦  np  
147170000   平壤  pr  
147180000   清津  qj  
147190000   沙里院 sly 
147200000   咸兴  xx  
147210000   新义州 xyz 
147220000   元山  ys  
148000000   丹麦  dm  
148110000   奥胡斯 ahs 
148120000   北日德兰    brdl    
148130000   博恩霍尔姆   behem   
148140000   菲特烈堡    ftlb    
148150000   菲茵  fy  
148160000   哥本哈根    gbhg    
148170000   里伯  lb  
148180000   灵克宾 lkb 
148190000   罗斯基勒    lsjl    
148200000   南日德兰    nrdl    
148210000   斯多斯特姆   sdstm   
148220000   维堡  wb  
148230000   维厄勒 wel 
148240000   西希兰 xxl 
149000000   德国  dg  
149110000   阿恩斯贝格   aesbg   
149120000   爱尔福特    aeft    
149130000   安斯巴格    asbg    
149140000   奥格斯堡    agsb    
149150000   柏林  bl  
149160000   拜伊罗特    bylt    
149170000   比勒费尔德   blfed   
149180000   波茨坦 bct 
149190000   波鸿  bh  
149200000   不来梅 blm 
149210000   不伦瑞克    blrk    
149220000   达姆施塔特   dmstt   
149230000   代特莫尔特   dtmet   
149240000   德累斯顿    dlsd    
149250000   德绍  ds  
149260000   杜塞尔多夫   dsedf   
149270000   法兰克福    flkf    
149280000   弗赖堡 flb 
149290000   哈雷  hl  
149300000   汉堡  hb  
149310000   汉诺威 hnw 
149320000   基尔  je  
149330000   吉森  js  
149340000   卡尔斯鲁厄   kesle   
149350000   卡塞尔 kse 
149360000   开姆尼斯    kmns    
149370000   科布伦次    kblc    
149380000   科隆  kl  
149390000   莱比锡 lbx 
149400000   兰茨胡特    lcht    
149410000   吕讷堡 lnb 
149420000   马格德堡    mgdb    
149430000   曼海姆 mhm 
149440000   美因兹 myz 
149450000   明斯特 mst 
149460000   慕尼黑 mnh 
149470000   纽伦堡 nlb 
149480000   什未林 swl 
149490000   斯图加特    stjt    
149500000   特里尔 tle 
149510000   威斯巴登    wsbd    
149520000   维尔茨堡    wecb    
150000000   东帝汶 ddw 
150110000   阿伊莱乌    aylw    
150120000   阿伊纳罗    aynl    
150130000   埃尔梅拉    aeml    
150140000   安贝诺 abn 
150150000   包考  bk  
150160000   博博纳罗    bbnl    
150170000   帝力  dl  
150180000   科瓦利马    kwlm    
150190000   劳滕  lt  
150200000   利基卡 ljk 
150210000   马纳图托    mntt    
150220000   马努法伊    mnfy    
150230000   维克克 wkk 
151000000   多哥  dg  
151110000   滨海区 bhq 
151120000   草原区 cyq 
151130000   高原区 gyq 
151140000   卡拉区 klq 
151150000   中部区 zbq 
152000000   多米尼加    dmnj    
153000000   多米尼加共和国 dmnjghg 
154000000   俄罗斯 els 
154110000   阿巴坎 abk 
154120000   阿尔汉格尔斯克 aehgesk 
154130000   阿金斯科耶   ajsky   
154140000   阿纳德尔    ande    
154150000   阿斯特拉罕   astlh   
154160000   埃利斯塔    alst    
154170000   奥廖尔 ale 
154180000   奥伦堡 alb 
154190000   巴尔瑙尔    bene    
154200000   奔萨  bs  
154210000   彼得罗巴甫洛夫斯克   bdlbflfsk   
154220000   彼得罗扎沃茨克 bdlzwck 
154230000   彼尔姆 bem 
154240000   比罗比詹    blbz    
154250000   别尔哥罗德   begld   
154260000   伯力  bl  
154270000   布拉戈维申斯克 blgwssk 
154280000   布良斯克    blsk    
154290000   车里雅宾斯克  clybsk  
154300000   赤塔  ct  
154310000   顿河畔罗斯托夫 dhplstf 
154320000   鄂木斯克    emsk    
154330000   伏尔加格勒   fejgl   
154340000   弗拉基米尔   fljme   
154350000   弗拉季高加索  fljgjs  
154360000   戈尔诺－阿尔泰斯克   gen－aetsk   
154370000   格罗兹尼    glzn    
154380000   海参崴 hcw 
154390000   汉特－曼西斯克 ht－mxsk 
154400000   基洛夫 jlf 
154410000   加里宁格勒   jlngl   
154420000   喀山  ks  
154430000   卡卢加 klj 
154440000   科斯特罗马   kstlm   
154450000   克拉斯诺达尔  klsnde  
154460000   克拉斯诺亚尔斯克    klsnyesk    
154470000   克麦罗沃    kmlw    
154480000   克孜勒 kzl 
154490000   库德姆卡尔   kdmke   
154500000   库尔干 keg 
154510000   库尔斯克    kesk    
154520000   利佩茨克    lpck    
154530000   梁赞  lz  
154540000   马哈奇卡拉   mhqkl   
154550000   马加丹 mjd 
154560000   马加斯 mjs 
154570000   迈科普 mkp 
154580000   摩尔曼斯克   memsk   
154590000   莫斯科 msk 
154600000   纳尔奇克    neqk    
154610000   纳里扬马尔   nlyme   
154620000   南萨哈林斯克  nshlsk  
154630000   诺夫哥罗德   nfgld   
154640000   帕拉纳 pln 
154650000   普斯科夫    pskf    
154660000   切博克萨雷   qbksl   
154670000   切尔克斯克   qeksk   
154680000   秋明  qm  
154690000   萨拉托夫    sltf    
154700000   萨兰斯克    slsk    
154710000   萨列哈尔德   slhed   
154720000   萨马拉 sml 
154730000   瑟克特夫卡尔  sktfke  
154740000   圣彼得堡    sbdb    
154750000   斯摩棱斯克   smlsk   
154760000   斯塔夫罗波尔  stflbe  
154770000   坦波夫 tbf 
154780000   特维尔 twe 
154790000   图拉  tl  
154800000   托木斯克    tmsk    
154810000   沃罗涅什    wlns    
154820000   沃洛格达    wlgd    
154830000   乌法  wf  
154840000   乌兰乌德    wlwd    
154850000   乌里扬诺夫斯克 wlynfsk 
154860000   乌斯季奥尔登斯基    wsjaedsj    
154870000   下诺夫哥罗德  xnfgld  
154880000   新西伯利亚   xxbly   
154890000   雅库茨克    ykck    
154900000   雅罗斯拉夫尔  ylslfe  
154910000   叶卡捷林堡   ykjlb   
154920000   伊尔库茨克   yekck   
154930000   伊热夫斯克   yrfsk   
154940000   伊万诺沃    ywnw    
154950000   约什卡尔奥拉  yskeal  
155000000   厄瓜多尔    egde    
155110000   阿苏艾 asa 
155120000   埃尔奥罗    aeal    
155130000   埃斯梅拉尔达斯 asmleds 
155140000   玻利瓦尔    blwe    
155150000   瓜亚斯 gys 
155160000   加拉帕戈斯   jlpgs   
155170000   卡尔奇 keq 
155180000   卡尼亚尔    knye    
155190000   科托帕希    ktpx    
155200000   洛哈  lh  
155210000   洛斯里奥斯   lslas   
155220000   马纳比 mnb 
155230000   莫罗纳－圣地亚哥    mln－sdyg    
155240000   纳波，奥雷利亚纳    nb，allyn    
155250000   帕斯塔萨    psts    
155260000   皮钦查 pqc 
155270000   钦博拉索    qbls    
155280000   萨莫拉－钦奇佩 sml－qqp 
155290000   苏昆毕奥斯   skbas   
155300000   通古拉瓦    tglw    
155310000   因巴布拉    ybbl    
156000000   厄立特里亚   eltly   
156110000   安塞巴 asb 
156120000   北红海 bhh 
156130000   加什·巴尔卡  js·bek  
156140000   南部  nb  
156150000   南红海 nhh 
156160000   中部  zb  
157000000   法国  fg  
157110000   阿尔勒 ael 
157120000   阿雅克修    aykx    
157130000   艾克斯 aks 
157140000   奥尔良 ael 
157150000   巴黎  bl  
157160000   贝桑松 bss 
157170000   第戎  dr  
157180000   弗雷瑞斯    flrs    
157190000   卡昂  ka  
157200000   雷恩  le  
157210000   里昂  la  
157220000   里尔  le  
157230000   利摩日 lmr 
157240000   鲁昂  la  
157250000   马赛  ms  
157260000   梅斯  ms  
157270000   蒙彼利埃    mbla    
157280000   南特  nt  
157290000   尼斯  ns  
157300000   沙隆  sl  
157310000   图卢兹 tlz 
157320000   瓦朗斯 wls 
157330000   亚眠  ym  
158000000   法罗群岛    flqd    
159000000   法属波利尼西亚 fsblnxy 
160000000   法属圭亚那   fsgyn   
161000000   法属南部领地  fsnbld  
162000000   梵蒂冈 fdg 
163000000   菲律宾 flb 
163110000   达沃  dw  
163120000   卡卢坎 klk 
163130000   马尼拉 mnl 
163140000   宿务  sw  
164000000   斐济  fj  
165000000   芬兰  fl  
165110000   埃斯波 asb 
165120000   奥卢  al  
165130000   波里  bl  
165140000   博尔沃 bew 
165150000   海门林纳    hmln    
165160000   赫尔辛基    hexj    
165170000   卡亚尼 kyn 
165180000   科科拉 kkl 
165190000   科特卡 ktk 
165200000   库奥皮奥    kapa    
165210000   拉赫蒂 lhd 
165220000   拉彭兰塔    lplt    
165230000   罗瓦涅米    lwnm    
165240000   玛丽港 mlg 
165250000   米凯利 mkl 
165260000   坦佩雷 tpl 
165270000   图尔库 tek 
165280000   瓦萨  ws  
165290000   万塔  wt  
165300000   约恩苏 yes 
166000000   佛得角 fdj 
166110000   保尔  be  
166120000   波多诺伏    bdnf    
166130000   博阿维斯塔岛  bawstd  
166140000   布拉瓦岛    blwd    
166150000   大里贝拉    dlbl    
166160000   福古岛 fgd 
166170000   马尤岛 myd 
166180000   莫斯特罗    mstl    
166190000   普拉亚 ply 
166200000   萨尔岛 sed 
166210000   圣安唐岛    satd    
166220000   圣地亚哥岛   sdygd   
166230000   圣多明戈    sdmg    
166240000   圣菲利普    sflp    
166250000   圣卡塔琳娜   sktln   
166260000   圣克鲁斯    skls    
166270000   圣米戈尔    smge    
166280000   圣尼古拉岛   sngld   
166290000   圣维森特岛   swstd   
166300000   塔拉法尔    tlfe    
167000000   弗兰克群岛   flkqd   
168000000   冈比亚 gby 
169000000   刚果  gg  
170000000   刚果民主共和国 ggmzghg 
171000000   哥伦比亚    glby    
171110000   阿劳卡 alk 
171120000   安提奥基亚   atajy   
171130000   北桑坦德    bstd    
171140000   波哥大首都区  bgdsdq  
171150000   博利瓦尔    blwe    
171160000   博亚卡 byk 
171170000   大西洋 dxy 
171180000   瓜维亚雷    gwyl    
171190000   瓜希拉 gxl 
171200000   瓜伊尼亚    gyny    
171210000   金迪奥 jda 
171220000   卡尔达斯    keds    
171230000   卡克塔 kkt 
171240000   卡萨纳雷    ksnl    
171250000   考卡  kk  
171260000   考卡山谷    kksg    
171270000   科尔多巴    kedb    
171280000   昆迪纳马卡   kdnmk   
171290000   利萨拉尔达   lsled   
171300000   马格达雷那   mgdln   
171310000   梅塔  mt  
171320000   纳里尼奥    nlna    
171330000   普图马约    ptmy    
171340000   乔科  qk  
171350000   塞萨尔 sse 
171360000   桑坦德 std 
171370000   圣安德烈斯-普罗维登西亚    sadls-plwdxy    
171380000   苏克雷 skl 
171390000   托利马 tlm 
171400000   维查达 wcd 
171410000   沃佩斯 wps 
171420000   乌伊拉 wyl 
171430000   亚马孙 yms 
172000000   哥斯达黎加   gsdlj   
172110000   阿拉胡埃拉   alhal   
172120000   埃雷迪亚    aldy    
172130000   瓜纳卡斯特   gnkst   
172140000   卡塔戈 ktg 
172150000   利蒙  lm  
172160000   蓬塔雷纳斯   ptlns   
172170000   圣何塞 shs 
173000000   格恩西岛    gexd    
174000000   格林纳达    glnd    
175000000   格陵兰 gll 
176000000   古巴  gb  
176110000   奥尔金 aej 
176120000   比那尔德里奥  bnedla  
176130000   比亚克拉拉   bykll   
176140000   格拉玛 glm 
176150000   关塔那摩    gtnm    
176160000   哈瓦那 hwn 
176170000   哈瓦那城    hwnc    
176180000   卡马圭 kmg 
176190000   拉斯图纳斯   lstns   
176200000   马坦萨斯    mtss    
176210000   马亚里 myl 
176220000   曼萨尼罗    msnl    
176230000   青年岛特区   qndtq   
176240000   圣地亚哥    sdyg    
176250000   圣斯皮里图斯  ssplts  
176260000   西恩富戈斯   xefgs   
176270000   谢戈德阿维拉  xgdawl  
177000000   瓜德罗普    gdlp    
178000000   关岛  gd  
179000000   圭亚那 gyn 
179110000   埃塞奎博群岛-西德梅拉拉    askbqd-xdmll    
179120000   巴里马-瓦伊尼 blm-wyn 
179130000   波默伦-苏佩纳姆    bml-spnm    
179140000   波塔罗-锡帕鲁尼    btl-xpln    
179150000   德梅拉拉-马海卡    dmll-mhk    
179160000   东伯比斯-科兰太因   dbbs-klty   
179170000   库尤尼-马扎鲁尼    kyn-mzln    
179180000   马海卡-伯比斯 mhk-bbs 
179190000   上德梅拉拉-伯比斯   sdmll-bbs   
179200000   上塔库图-上埃塞奎博  stkt-saskb  
180000000   哈萨克斯坦   hskst   
180110000   阿尔卡累克   aeklk   
180120000   阿克莫拉    akml    
180130000   阿克苏 aks 
180140000   阿克托别    aktb    
180150000   阿拉木图    almt    
180160000   阿雷斯 als 
180170000   阿斯塔纳市   astns   
180180000   阿特劳 atl 
180190000   埃基巴斯图兹  ajbstz  
180200000   巴尔喀什    beks    
180210000   巴甫洛达尔   bflde   
180220000   北哈萨克斯坦  bhskst  
180230000   东哈萨克斯坦  dhskst  
180240000   济良诺夫斯克  jlnfsk  
180250000   江布尔 jbe 
180260000   杰兹卡兹甘   jzkzg   
180270000   卡拉干达    klgd    
180280000   卡拉扎尔    klze    
180290000   卡普恰盖    kpqg    
180300000   科斯塔奈    kstn    
180310000   克孜勒奥尔达  kzlaed  
180320000   肯套  kt  
180330000   库尔恰托夫   keqtf   
180340000   利萨科夫斯克  lskfsk  
180350000   列宁诺戈尔斯克 lnngesk 
180360000   鲁德内 ldn 
180370000   曼格斯套    mgst    
180380000   南哈萨克斯坦  nhskst  
180390000   萨兰  sl  
180400000   塞梅伊 smy 
180410000   沙赫京斯克   shjsk   
180420000   斯捷普诺戈尔斯克    sjpngesk    
180430000   铁克利 tkl 
180440000   铁米尔套    tmet    
180450000   突厥斯坦    tjst    
180460000   西哈萨克斯坦  xhskst  
180470000   扎纳奥津    znaj    
181000000   海地  hd  
182000000   韩国  hg  
182110000   大邱  dq  
182110100   达城郡 dcj 
182110200   大邱  dq  
182110300   寿城区 scq 
182120000   大田  dt  
182130000   釜山  fs  
182140000   光州  gz  
182150000   济州特别自治道 jztbzzd 
182160000   江原道 jyd 
182160100   春川市 ccs 
182160200   东海市 dhs 
182160300   高城郡 gcj 
182160400   横城郡 hcj 
182160500   洪川郡 hcj 
182160600   华川郡 hcj 
182160700   江陵市 jls 
182160800   旌善郡 jsj 
182160900   麟蹄郡 ltj 
182161000   宁越郡 nyj 
182161100   平昌郡 pcj 
182161200   三陟市 szs 
182161300   束草市 scs 
182161400   太白市 tbs 
182161500   铁原郡 tyj 
182161600   襄阳郡 xyj 
182161700   杨口郡 ykj 
182161800   原州市 yzs 
182170000   京畿道 jjd 
182170100   安城市 acs 
182170200   安山市 ass 
182170300   安养市 ays 
182170400   抱川市 bcs 
182170500   城南市 cns 
182170600   东豆川市    ddcs    
182170700   富川市 fcs 
182170800   高阳市 gys 
182170900   光明市 gms 
182171000   广州市 gzs 
182171100   果川市 gcs 
182171200   河南市 hns 
182171300   华城市 hcs 
182171400   加平郡 jpj 
182171500   金浦市 jps 
182171600   九里市 jls 
182171700   军浦市 jps 
182171800   骊州郡 lzj 
182171900   利川市 lcs 
182172000   涟川郡 lcj 
182172100   龙仁市 lrs 
182172200   南杨州市    nyzs    
182172300   平泽市 pzs 
182172400   坡州市 pzs 
182172500   始兴市 sxs 
182172600   水原市 sys 
182172700   乌山市 wss 
182172800   扬平郡 ypj 
182172900   杨州市 yzs 
182173000   仪旺市 yws 
182173100   议政府市    yzfs    
182180000   庆尚北道    qsbd    
182180100   安东市 ads 
182180200   奉化郡 fhj 
182180300   高灵郡 glj 
182180400   龟尾市 gws 
182180500   金泉市 jqs 
182180600   军威郡 jwj 
182180700   醴泉郡 lqj 
182180800   浦项市 pxs 
182180900   漆谷郡 qgj 
182181000   淸道郡 qdj 
182181100   靑松郡 qsj 
182181200   庆山市 qss 
182181300   庆州市 qzs 
182181400   荣州市 rzs 
182181500   尙州市 szs 
182181600   蔚珍郡 yzj 
182181700   闻庆市 wqs 
182181800   星州郡 xzj 
182181900   义城郡 ycj 
182182000   英阳郡 yyj 
182182100   盈德郡 ydj 
182182200   永川市 ycs 
182182300   郁陵郡 ylj 
182190000   庆尚南道    qsnd    
182190100   昌宁郡 cnj 
182190200   昌原市 cys 
182190300   固城郡 gcj 
182190400   河东郡 hdj 
182190500   金海市 jhs 
182190600   晋州市 jzs 
182190700   居昌郡 jcj 
182190800   巨济市 jjs 
182190900   梁山市 lss 
182191000   马山市 mss 
182191100   密阳市 mys 
182191200   南海郡 nhj 
182191300   山淸郡 sqj 
182191400   泗川市 scs 
182191500   统营市 tys 
182191600   陜川郡 scj 
182191700   咸安郡 xaj 
182191800   咸阳郡 xyj 
182191900   宜宁郡 ynj 
182192000   鎭海市 zhs 
182200000   全罗北道    qlbd    
182200100   淳昌郡 ccj 
182200200   扶安郡 faj 
182200300   高敞郡 gcj 
182200400   金堤市 jds 
182200500   井邑市 jys 
182200600   茂朱郡 mzj 
182200700   南原市 nys 
182200800   全州市 qzs 
182200900   群山市 qss 
182201000   任实郡 rsj 
182201100   完州郡 wzj 
182201200   益山市 yss 
182201300   长水郡 zsj 
182201400   鎭安郡 zaj 
182210000   全罗南道    qlnd    
182210100   宝城郡 bcj 
182210200   高兴郡 gxj 
182210300   谷城郡 gcj 
182210400   莞岛郡 gdj 
182210500   光阳市 gys 
182210600   海南郡 hnj 
182210700   和顺郡 hsj 
182210800   康津郡 kjj 
182210900   丽水市 lss 
182211000   灵光郡 lgj 
182211100   灵岩郡 lyj 
182211200   罗州市 lzs 
182211300   木浦市 mps 
182211400   求礼郡 qlj 
182211500   顺天市 sts 
182211600   潭阳郡 tyj 
182211700   务安郡 waj 
182211800   咸平郡 xpj 
182211900   新安郡 xaj 
182212000   长城郡 zcj 
182212100   长兴郡 zxj 
182212200   珍岛郡 zdj 
182220000   仁川  rc  
182230000   首尔  se  
182240000   蔚山  ys  
182250000   忠清北道    zqbd    
182250100   报恩郡 bej 
182250200   曾坪郡 cpj 
182250300   丹阳郡 dyj 
182250400   堤川市 dcs 
182250500   槐山郡 hsj 
182250600   淸原郡 qyj 
182250700   淸州市 qzs 
182250800   沃川郡 wcj 
182250900   阴城郡 ycj 
182251000   永同郡 ytj 
182251100   鎭川郡 zcj 
182251200   忠州市 zzs 
182260000   忠清南道    zqnd    
182260100   保宁市 bns 
182260200   扶余郡 fyj 
182260300   公州市 gzs 
182260400   洪城郡 hcj 
182260500   鸡龙市 jls 
182260600   锦山郡 jsj 
182260700   礼山郡 lsj 
182260800   论山市 lss 
182260900   青阳郡 qyj 
182261000   瑞山市 rss 
182261100   舒川郡 scj 
182261200   泰安郡 taj 
182261300   唐津郡 tjj 
182261400   天安市 tas 
182261500   牙山市 yss 
182261600   燕岐郡 yqj 
183000000   荷兰  hl  
183110000   阿尔梅勒    aeml    
183120000   阿默斯福特   amsft   
183130000   阿姆斯特丹   amstd   
183140000   阿纳姆 anm 
183150000   阿珀尔多伦   apedl   
183160000   阿森  as  
183170000   埃德  ad  
183180000   埃门  am  
183190000   埃因霍芬    ayhf    
183200000   布雷达 bld 
183210000   蒂尔堡 deb 
183220000   多德雷赫特   ddlht   
183230000   恩斯赫德    eshd    
183240000   格罗宁根    glng    
183250000   哈勒姆 hlm 
183260000   海牙  hy  
183270000   霍夫多尔普   hfdep   
183280000   莱顿  ld  
183290000   莱利斯塔德   llstd   
183300000   鹿特丹 ltd 
183310000   吕伐登 lfd 
183320000   马斯特里赫特  mstlht  
183330000   米德尔堡    mdeb    
183340000   奈梅亨 nmh 
183350000   斯海尔托亨博思 shethbs 
183360000   乌得勒支    wdlz    
183370000   兹沃勒 zwl 
183380000   佐特尔梅    ztem    
184000000   荷属安地列斯  hsadls  
185000000   赫德和麦克唐纳群岛   hdhmktnqd   
186000000   洪都拉斯    hdls    
186110000   阿特兰蒂达   atldd   
186120000   埃尔帕拉伊索  aeplys  
186130000   奥科特佩克   aktpk   
186140000   奥兰乔 alq 
186150000   弗朗西斯科-莫拉桑   flxsk-mls   
186160000   格拉西亚斯-阿迪奥斯  glxys-adas  
186170000   海湾群岛    hwqd    
186180000   科尔特斯    kets    
186190000   科隆  kl  
186200000   科马亚瓜    kmyg    
186210000   科潘  kp  
186220000   拉巴斯 lbs 
186230000   伦皮拉 lpl 
186240000   乔卢特卡    qltk    
186250000   乔罗马 qlm 
186260000   山谷  sg  
186270000   圣巴巴拉    sbbl    
186280000   因蒂布卡    ydbk    
186290000   约罗  yl  
187000000   基里巴斯    jlbs    
187110000   菲尼克斯群岛  fnksqd  
187120000   吉尔伯特群岛  jebtqd  
187130000   莱恩群岛    leqd    
188000000   吉布提 jbt 
188110000   阿里萨比赫区  alsbhq  
188120000   奥博克区    abkq    
188130000   迪基勒区    djlq    
188140000   塔朱拉区    tzlq    
189000000   吉尔吉斯斯坦  jejsst  
189110000   奥什  as  
189120000   巴特肯 btk 
189130000   比什凯克市   bskks   
189140000   楚河  ch  
189150000   贾拉拉巴德   jllbd   
189160000   卡拉巴尔塔   klbet   
189170000   卡拉库尔    klke    
189180000   坎特  kt  
189190000   科克扬加克   kkyjk   
189200000   迈利赛 mls 
189210000   纳伦  nl  
189220000   苏卢克图    slkt    
189230000   塔拉斯 tls 
189240000   塔什库梅尔   tskme   
189250000   乌兹根 wzg 
189260000   伊塞克湖    yskh    
190000000   几内亚 jny 
190110000   博凯  bk  
190120000   恩泽雷科雷   ezlkl   
190130000   法拉纳 fln 
190140000   金迪亚 jdy 
190150000   康康  kk  
190160000   科纳克里    knkl    
190170000   拉贝  lb  
190180000   玛木  mm  
191000000   几内亚比绍   jnybs   
192000000   加拿大 jnd 
192110000   阿伯茨福    abcf    
192120000   埃德蒙顿    admd    
192130000   奥沙瓦 asw 
192140000   巴里  bl  
192150000   布列塔尼角   bltnj   
192160000   多伦多 dld 
192170000   弗雷德里顿   fldld   
192180000   圭尔夫 gef 
192190000   哈利法克斯   hlfks   
192200000   哈密尔顿    hmed    
192210000   怀特霍斯    hths    
192220000   基劳纳 jln 
192230000   基奇纳 jqn 
192240000   金斯敦 jsd 
192250000   卡里加里    kljl    
192260000   魁北克 kbk 
192270000   里贾纳 ljn 
192280000   伦敦  ld  
192290000   蒙特利尔    mtle    
192300000   萨德伯里    sdbl    
192310000   萨斯卡通    sskt    
192320000   三河城 shc 
192330000   桑德贝 sdb 
192340000   舍布鲁克    sblk    
192350000   圣卡塔琳娜   sktln   
192360000   圣约翰斯    syhs    
192370000   维多利亚    wdly    
192380000   温哥华 wgh 
192390000   温尼伯 wnb 
192400000   温莎  ws  
192410000   渥太华 wth 
192420000   夏洛特敦    xltd    
192430000   耶洛奈夫    ylnf    
192440000   伊魁特 ykt 
193000000   加纳  jn  
193110000   阿散蒂 asd 
193120000   奥布阿西    abax    
193130000   北部  bb  
193140000   布朗阿哈福   blahf   
193150000   大阿克拉    dakl    
193160000   东部  db  
193170000   上东部 sdb 
193180000   上西部 sxb 
193190000   沃尔特 wet 
193200000   西部  xb  
193210000   中部  zb  
194000000   加蓬  jp  
194110000   奥果韦-洛洛  agw-ll  
194120000   奥果韦-伊温多 agw-ywd 
194130000   滨海奥果韦   bhagw   
194140000   恩古涅 egn 
194150000   河口  hk  
194160000   尼扬加 nyj 
194170000   上奥果韦    sagw    
194180000   沃勒-恩特姆  wl-etm  
194190000   中奥果韦    zagw    
195000000   柬埔寨 jpz 
195110000   奥多棉吉    admj    
195120000   白马市 bms 
195130000   柏威夏 bwx 
195140000   拜林市 bls 
195150000   班迭棉吉    bdmj    
195160000   磅清扬 bqy 
195170000   磅士卑 bsb 
195180000   磅同  bt  
195190000   磅湛  bz  
195200000   波罗勉 blm 
195210000   茶胶  cj  
195220000   柴桢  cz  
195230000   干丹  gd  
195240000   戈公  gg  
195250000   贡布  gb  
195260000   金边市 jbs 
195270000   桔井  jj  
195280000   腊塔纳基里   ltnjl   
195290000   马德望 mdw 
195300000   蒙多基里    mdjl    
195310000   菩萨  ps  
195320000   上丁  sd  
195330000   西哈努克市   xhnks   
195340000   暹粒  xl  
196000000   捷克共和国   jkghg   
196110000   奥洛穆茨    almc    
196120000   比尔森 bes 
196130000   布拉格直辖市  blgzxs  
196140000   赫拉德茨-克拉洛韦   hldc-kllw   
196150000   卡罗维发利   klwfl   
196160000   利贝雷克    lblk    
196170000   摩拉维亚-西里西亚   mlwy-xlxy   
196180000   南摩拉维亚   nmlwy   
196190000   帕尔杜比采   pedbc   
196200000   维索基纳    wsjn    
196210000   乌斯季 wsj 
196220000   中捷克 zjk 
196230000   兹林  zl  
197000000   津巴布韦    jbbw    
197110000   北马塔贝莱兰  bmtbll  
197120000   布拉瓦约    blwy    
197130000   东马绍纳兰   dmsnl   
197140000   哈拉雷 hll 
197150000   马尼卡兰    mnkl    
197160000   马斯温戈    mswg    
197170000   南马塔贝莱兰  nmtbll  
197180000   西马绍纳兰   xmsnl   
197190000   中部  zb  
197200000   中马绍纳兰   zmsnl   
198000000   喀麦隆 kml 
198110000   阿达马瓦    admw    
198120000   北部  bb  
198130000   北端  bd  
198140000   滨海  bh  
198150000   东部  db  
198160000   南部  nb  
198170000   西北  xb  
198180000   西部  xb  
198190000   西南  xn  
198200000   中央  zy  
199000000   卡塔尔 kte 
199110000   北部  bb  
199120000   多哈  dh  
199130000   古韦里耶    gwly    
199140000   豪尔  he  
199150000   杰里扬拜特奈  jlybtn  
199160000   赖扬  ly  
199170000   沃克拉 wkl 
199180000   乌姆锡拉勒   wmxll   
199190000   朱迈利耶    zmly    
200000000   开曼群岛    kmqd    
201000000   科科斯群岛   kksqd   
202000000   科摩罗 kml 
203000000   科特迪瓦    ktdw    
203110000   阿涅比 anb 
203120000   巴芬  bf  
203130000   邦达马河谷   bdmhg   
203140000   登盖莱 dgl 
203150000   恩济－科莫埃  ej－kma  
203160000   弗罗马格尔   flmge   
203170000   湖泊  hb  
203180000   马拉韦 mlw 
203190000   南邦达马    nbdm    
203200000   南科莫埃    nkma    
203210000   萨桑德拉    ssdl    
203220000   萨瓦纳 swn 
203230000   山地  sd  
203240000   沃罗杜古    wldg    
203250000   下萨桑德拉   xssdl   
203260000   泻湖  xh  
203270000   赞赞  zz  
203280000   中卡瓦利    zkwl    
203290000   中科莫埃    zkma    
204000000   科威特 kwt 
205000000   克罗地亚    kldy    
205110000   奥西耶克-巴拉尼亚   axyk-blny   
205120000   别洛瓦尔-比洛戈拉   blwe-blgl   
205130000   滨海和山区   bhhsq   
205140000   波热加-斯拉沃尼亚   brj-slwny   
205150000   布罗德-波萨维纳    bld-bswn    
205160000   杜布罗夫斯克-内雷特瓦 dblfsk-nltw 
205170000   卡尔洛瓦茨   kelwc   
205180000   科普里夫尼察-克里热夫齐    kplfnc-klrfq    
205190000   克拉皮纳-扎戈列    klpn-zgl    
205200000   利卡-塞尼   lk-sn   
205210000   梅吉穆列    mjml    
205220000   萨格勒布    sglb    
205230000   萨格勒布市   sglbs   
205240000   斯普利特-达尔马提亚  splt-demty  
205250000   瓦拉日丁    wlrd    
205260000   维罗维蒂察-波德拉维纳 wlwdc-bdlwn 
205270000   武科瓦尔-斯里耶姆   wkwe-slym   
205280000   希贝尼克-克宁 xbnk-kn 
205290000   锡萨克-莫斯拉维纳   xsk-mslwn   
205300000   伊斯特拉    ystl    
205310000   扎达尔 zde 
206000000   肯尼亚 kny 
206110000   埃尔格约-马拉奎特   aegy-mlkt   
206120000   巴林戈 blg 
206130000   邦戈马 bgm 
206140000   博美特 bmt 
206150000   布希亚 bxy 
206160000   恩布  eb  
206170000   霍马湾 hmw 
206180000   基安布 jab 
206190000   基里菲 jlf 
206200000   基里尼亚加   jlnyj   
206210000   基苏木 jsm 
206220000   基图伊 jty 
206230000   基西  jx  
206240000   加里萨 jls 
206250000   卡卡梅加    kkmj    
206260000   卡耶亚多    kyyd    
206270000   凯里乔 klq 
206280000   夸勒  kl  
206290000   拉木  lm  
206300000   莱基皮亚    ljpy    
206310000   马查科斯    mcks    
206320000   马瓜尼 mgn 
206330000   马萨布布    msbb    
206340000   曼德拉 mdl 
206350000   梅鲁  ml  
206360000   蒙巴萨 mbs 
206370000   米戈利 mgl 
206380000   穆兰卡 mlk 
206390000   纳库鲁 nkl 
206400000   纳罗克 nlk 
206410000   南迪  nd  
206420000   内罗毕 nlb 
206430000   尼蒂  nd  
206440000   尼亚米拉    nyml    
206450000   年达鲁阿    ndla    
206460000   涅里  nl  
206470000   桑布卢 sbl 
206480000   塔纳河 tnh 
206490000   泰塔塔维塔   tttwt   
206500000   特兰斯-恩佐亚 tls-ezy 
206510000   图尔卡纳    tekn    
206520000   瓦吉尔 wje 
206530000   瓦辛基苏    wxjs    
206540000   韦希加 wxj 
206550000   西波克特    xbkt    
206560000   夏亚  xy  
206570000   伊希约洛    yxyl    
206580000   中央  zy  
207000000   库克群岛    kkqd    
208000000   拉脱维亚    ltwy    
208110000   阿卢克斯内   alksn   
208120000   爱兹克劳克雷  azklkl  
208130000   奥格雷 agl 
208140000   巴尔维 bew 
208150000   包斯卡 bsk 
208160000   采西斯 cxs 
208170000   多贝莱 dbl 
208180000   古尔贝内    gebn    
208190000   杰卡布皮尔斯  jkbpes  
208200000   克拉斯拉瓦   klslw   
208210000   库尔迪加    kedj    
208220000   雷泽克内    lzkn    
208230000   里加  lj  
208240000   利耶帕亚    lypy    
208250000   林巴济 lbj 
208260000   卢扎  lz  
208270000   马多纳 mdn 
208280000   普雷利 pll 
208290000   萨尔杜斯    seds    
208300000   塔尔西 tex 
208310000   陶格夫皮尔斯  tgfpes  
208320000   图库马 tkm 
208330000   瓦尔加 wej 
208340000   瓦尔米耶拉   wemyl   
208350000   文茨皮尔斯   wcpes   
208360000   叶尔加瓦    yejw    
209000000   莱索托 lst 
209110000   伯里亚 bly 
209120000   布塔布泰    btbt    
209130000   古廷  gt  
209140000   加查斯内克   jcsnk   
209150000   莱里贝 llb 
209160000   马费滕 mft 
209170000   马塞卢 msl 
209180000   莫哈莱斯胡克  mhlshk  
209190000   莫霍特隆    mhtl    
209200000   塔巴采卡    tbck    
210000000   老挝  lw  
210110000   阿速坡 asp 
210120000   波里坎赛    blks    
210130000   博乔  bq  
210140000   川圹  ck  
210150000   丰沙里 fsl 
210160000   甘蒙  gm  
210170000   华潘  hp  
210180000   琅勃拉邦    lblb    
210190000   琅南塔 lnt 
210200000   赛宋本行政特区 ssbxztq 
210210000   色贡  sg  
210220000   沙拉湾 slw 
210230000   沙湾拿吉    swnj    
210240000   沙耶武里    sywl    
210250000   万象  wx  
210260000   乌多姆赛    wdms    
210270000   占巴塞 zbs 
211000000   黎巴嫩 lbn 
211110000   北部  bb  
211120000   贝卡  bk  
211130000   贝鲁特 blt 
211140000   黎巴嫩山    lbns    
211150000   奈拜提耶市   nbtys   
211160000   南部  nb  
212000000   利比里亚    lbly    
212110000   巴波卢 bbl 
212120000   邦   b   
212130000   博波卢 bbl 
212140000   博米  bm  
212150000   大巴萨 dbs 
212160000   大吉德 djd 
212170000   大角山 djs 
212180000   大克鲁 dkl 
212190000   菲什敦 fsd 
212200000   吉河  jh  
212210000   里弗塞斯    lfss    
212220000   洛法  lf  
212230000   马吉比 mjb 
212240000   马里兰 mll 
212250000   蒙特塞拉多   mtsld   
212260000   宁巴  nb  
212270000   锡诺  xn  
213000000   利比亚 lby 
214000000   立陶宛 ltw 
214110000   阿利图斯    alts    
214120000   考纳斯 kns 
214130000   克莱佩达    klpd    
214140000   马里扬泊列   mlybl   
214150000   帕涅韦日斯   pnwrs   
214160000   陶拉格 tlg 
214170000   特尔希艾    texa    
214180000   维尔纽斯    wens    
214190000   乌田纳 wtn 
214200000   希奥利艾    xala    
214210000   亚克曼 ykm 
215000000   列支敦士登   lzdsd   
216000000   留尼旺岛    lnwd    
217000000   卢森堡 lsb 
217110000   迪基希 djx 
217120000   格雷文马赫   glwmh   
217130000   卢森堡 lsb 
218000000   卢旺达 lwd 
218110000   比温巴 bwb 
218120000   布塔雷 btl 
218130000   恩延扎 eyz 
218140000   基本古 jbg 
218150000   基布耶 jby 
218160000   基加利-恩加利 jjl-ejl 
218170000   基加利市    jjls    
218180000   吉孔戈罗    jkgl    
218190000   吉塞尼 jsn 
218200000   吉塔拉马    jtlm    
218210000   卡布加 kbj 
218220000   卢瓦马加纳   lwmjn   
218230000   鲁汉戈 lhg 
218240000   鲁亨盖里    lhgl    
218250000   尚古古 sgg 
218260000   乌姆塔拉    wmtl    
219000000   罗马尼亚    lmny    
219110000   阿尔巴尤利亚  aebyly  
219120000   阿拉德 ald 
219130000   奥拉迪亚    aldy    
219140000   巴克乌 bkw 
219150000   巴亚马雷    byml    
219160000   比斯特里察   bstlc   
219170000   博托沙尼    btsn    
219180000   布加勒斯特   bjlst   
219190000   布拉索夫    blsf    
219200000   布勒伊拉    blyl    
219210000   布泽乌 bzw 
219220000   德罗贝塔-塞维林堡   dlbt-swlb   
219230000   德瓦  dw  
219240000   蒂米什瓦拉   dmswl   
219250000   福克沙尼    fksn    
219260000   加拉茨 jlc 
219270000   久尔久 jej 
219280000   康斯坦察    kstc    
219290000   克拉约瓦    klyw    
219300000   克勒拉希    kllx    
219310000   克卢日纳波卡  klrnbk  
219320000   勒姆尼库沃尔恰 lmnkweq 
219330000   雷希察 lxc 
219340000   梅尔库里亚丘克 meklyqk 
219350000   皮特什蒂    ptsd    
219360000   皮亚特拉尼亚姆茨    pytlnymc    
219370000   普洛耶什蒂   plysd   
219380000   萨图·马雷   st·ml   
219390000   圣格奥尔基   sgaej   
219400000   斯拉蒂纳    sldn    
219410000   斯洛博齐亚   slbqy   
219420000   苏恰瓦 sqw 
219430000   特尔戈维什泰  tegwst  
219440000   特尔古穆列什  tegmls  
219450000   特尔古日乌   tegrw   
219460000   图尔恰 teq 
219470000   瓦斯卢伊    wsly    
219480000   锡比乌 xbw 
219490000   雅西  yx  
219500000   亚厉山德里亚  ylsdly  
219510000   扎勒乌 zlw 
220000000   马达加斯加   mdjsj   
220110000   安齐拉纳纳   aqlnn   
220120000   菲亚纳兰楚阿  fynlca  
220130000   马哈赞加    mhzj    
220140000   塔那那利佛   tnnlf   
220150000   图阿马西拉   tamxl   
220160000   图利亚拉    tlyl    
221000000   马尔代夫    medf    
221110000   阿杜  ad  
221120000   北阿里 bal 
221130000   北蒂拉杜马蒂  bdldmd  
221140000   北马洛斯马杜卢 bmlsmdl 
221150000   北米拉杜马杜卢 bmldmdl 
221160000   北尼兰杜    bnld    
221170000   北苏瓦迪瓦   bswdw   
221180000   法迪福卢    fdfl    
221190000   费利杜 fld 
221200000   福阿穆拉库   famlk   
221210000   哈杜马蒂    hdmd    
221220000   科卢马杜卢   klmdl   
221230000   马累  ml  
221240000   马累岛 mld 
221250000   穆拉库 mlk 
221260000   南阿里 nal 
221270000   南蒂拉杜马蒂  ndldmd  
221280000   南马洛斯马杜卢 nmlsmdl 
221290000   南米拉杜马杜卢 nmldmdl 
221300000   南尼兰杜    nnld    
221310000   南苏瓦迪瓦   nswdw   
222000000   马耳他 met 
223000000   马拉维 mlw 
223110000   北部区 bbq 
223120000   南部区 nbq 
223130000   中央区 zyq 
224000000   马来西亚    mlxy    
224110000   槟榔屿 bly 
224110100   北海  bh  
224110200   槟城  bc  
224110300   大山脚 dsj 
224110400   高渊  gy  
224120000   玻璃市 bls 
224120100   加央  jy  
224130000   丁加奴 djn 
224130100   甘马挽 gmw 
224130200   瓜拉丁加奴   gldjn   
224130300   龙运  ly  
224130400   马江  mj  
224130500   实兆  sz  
224130600   乌鲁  wl  
224130700   勿述  ws  
224140000   吉打  jd  
224140100   巴东得腊    bddl    
224140200   笨筒  bt  
224140300   浮罗交怡    fljy    
224140400   哥打士打    gdsd    
224140500   古邦巴素    gbbs    
224140600   瓜拉姆达    glmd    
224140700   华玲  hl  
224140800   居林  jl  
224140900   万拉峇鲁    wlkl    
224150000   吉兰丹 jld 
224150100   巴西富地    bxfd    
224150200   巴西马 bxm 
224150300   丹那美拉    dnml    
224150400   道北  db  
224150500   登卓  dz  
224150600   哥打巴鲁    gdbl    
224150700   瓜拉吉赖    gljl    
224150800   话望生 hws 
224150900   马樟  mz  
224151000   日里  rl  
224160000   吉隆坡 jlp 
224160100   吉隆坡 jlp 
224170000   马六甲 mlj 
224170100   马六甲市    mljs    
224170200   亚罗牙也    ylyy    
224170300   野新  yx  
224180000   纳闽  nm  
224180100   纳闽  nm  
224180200   维多利亚    wdly    
224190000   彭亨  ph  
224190100   百乐  bl  
224190200   北根  bg  
224190300   淡马鲁 dml 
224190400   而连突 elt 
224190500   关丹  gd  
224190600   金马仑高原   jmlgy   
224190700   劳勿  lw  
224190800   立卑  lb  
224190900   马兰  ml  
224191000   文冬  wd  
224191100   云冰  yb  
224200000   霹雳  pl  
224200100   安顺  as  
224200200   丹绒马 drm 
224200300   和丰  hf  
224200400   紅土坎 htk 
224200500   华都牙也    hdyy    
224200600   江沙  js  
224200700   太平  tp  
224200800   怡保  yb  
224210000   柔佛  rf  
224210100   笨珍  bz  
224210200   丰盛港 fsg 
224210300   哥打丁宜    gddy    
224210400   居銮  jl  
224210500   峇株巴辖    kzbx    
224210600   麻坡  mp  
224210700   昔加末 xjm 
224210800   新山  xs  
224220000   森美兰 sml 
224220100   波德申 bds 
224220200   淡边  db  
224220300   芙蓉  fr  
224220400   瓜拉庇劳    glbl    
224220500   林茂  lm  
224220600   仁保  rb  
224220700   日叻务 rlw 
224230000   沙巴  sb  
224230100   吧巴  bb  
224230200   保佛  bf  
224230300   比鲁兰 bll 
224230400   必达士 bds 
224230500   兵南邦 bnb 
224230600   担布南 dbn 
224230700   丹南  dn  
224230800   斗湖  dh  
224230900   斗亚兰 dyl 
224231000   哥打基纳巴鲁  gdjnbl  
224231100   哥打马鲁都   gdmld   
224231200   根地咬 gdy 
224231300   古达  gd  
224231400   古打毛律    gdml    
224231500   古纳  gn  
224231600   瓜拉班尤    glby    
224231700   京那巴登岸   jnbda   
224231800   兰脑  ln  
224231900   拿笃  nd  
224232000   纳巴湾 nbw 
224232100   山打根 sdg 
224232200   西比陶 xbt 
224232300   仙本那 xbn 
224240000   沙捞越 sly 
224240100   古晋  gj  
224240200   加帛  jb  
224240300   林梦  lm  
224240400   美里  ml  
224240500   民都鲁 mdl 
224240600   木胶  mj  
224240700   木中  mz  
224240800   三马拉汉    smlh    
224240900   斯里阿曼    slam    
224241000   泗里街 slj 
224241100   泗务  sw  
224250000   雪兰莪 xle 
224250100   八打灵 bdl 
224250200   鹅麦  em  
224250300   瓜拉冷岳    glly    
224250400   瓜拉雪兰莪   glxle   
224250500   沙白安南    sban    
224250600   乌鲁冷岳    wlly    
224250700   乌鲁雪兰莪   wlxle   
224250800   雪邦  xb  
225000000   马里  ml  
225110000   巴马科首都区  bmksdq  
225120000   基达尔 jde 
225130000   加奥  ja  
225140000   卡伊  ky  
225150000   库利科罗    klkl    
225160000   莫普提 mpt 
225170000   塞古  sg  
225180000   通布图 tbt 
225190000   锡卡索 xks 
226000000   马其顿 mqd 
227000000   马绍尔群岛   mseqd   
228000000   马提尼克    mtnk    
229000000   马约特岛    mytd    
230000000   曼岛  md  
231000000   毛里求斯    mlqs    
232000000   毛里塔尼亚   mltny   
232110000   阿德拉尔    adle    
232120000   阿萨巴 asb 
232130000   卜拉克纳    blkn    
232140000   东胡德 dhd 
232150000   戈尔戈勒    gegl    
232160000   吉迪马卡    jdmk    
232170000   努瓦迪布湾   nwdbw   
232180000   努瓦克肖特特区 nwkxttq 
232190000   塔甘特 tgt 
232200000   特拉扎 tlz 
232210000   提里斯-宰穆尔 tls-zme 
232220000   西胡德 xhd 
232230000   因希里 yxl 
233000000   美国  mg  
233110000   阿肯色 aks 
233110100   费耶特维尔   fytwe   
233110200   史密斯堡    smsb    
233110300   小石城 xsc 
233120000   阿拉巴马    albm    
233120100   伯明罕 bmh 
233120200   蒙哥马利    mgml    
233120300   莫比尔 mbe 
233130000   阿拉斯加    alsj    
233130100   安克雷奇    aklq    
233130200   费尔班克斯   febks   
233130300   朱诺  zn  
233140000   爱达荷 adh 
233140100   爱达荷福尔斯  adhfes  
233140200   波卡特洛    bktl    
233140300   博伊西 byx 
233140400   布莱克富特   blkft   
233140500   科达伦 kdl 
233140600   刘易斯顿    lysd    
233140700   莫斯科 msk 
233140800   墨菲  mf  
233140900   楠帕  np  
233141000   岂彻姆 qcm 
233141100   森瓦利 swl 
233141200   亚美利加瀑布城 ymljpbc 
233150000   爱荷华 ahh 
233150100   达文波特    dwbt    
233150200   得梅因 dmy 
233150300   锡达拉皮兹   xdlpz   
233160000   北达科他    bdkt    
233160100   俾斯麦 bsm 
233160200   大福克斯    dfks    
233160300   法戈  fg  
233160400   迈诺特 mnt 
233170000   北卡罗来纳   bklln   
233170100   艾许维尔    axwe    
233170200   杜罕  dh  
233170300   格林斯伯勒   glsbl   
233170400   教堂山 jts 
233170500   罗利  ll  
233170600   洛利杜罕都会区 lldhdhq 
233170700   夏洛特 xlt 
233180000   宾夕法尼亚   bxfny   
233180100   阿伦敦 ald 
233180200   费城  fc  
233180300   匹兹堡 pzb 
233190000   德克萨斯    dkss    
233190100   埃尔帕索    aeps    
233190200   奥斯汀 ast 
233190300   达拉斯 dls 
233190400   哥帕斯基斯蒂  gpsjsd  
233190500   交维斯顿    jwsd    
233190600   拉雷多 lld 
233190700   麦亚伦 myl 
233190800   圣安东尼奥   sadna   
233190900   休斯敦 xsd 
233200000   俄亥俄 ehe 
233200100   代顿  dd  
233200200   哥伦布 glb 
233200300   克利夫兰    klfl    
233200400   托莱多 tld 
233200500   辛辛那提    xxnt    
233210000   俄克拉荷马   eklhm   
233210100   俄克拉荷马城  eklhmc  
233210200   诺曼  nm  
233210300   塔尔萨 tes 
233220000   俄勒冈 elg 
233220100   本德  bd  
233220200   波特兰 btl 
233220300   达尔斯 des 
233220400   达拉斯 dls 
233220500   蒂拉穆克    dlmk    
233220600   格兰茨帕斯   glcps   
233220700   胡德里弗    hdlf    
233220800   火山口湖    hskh    
233220900   科瓦利斯    kwls    
233221000   库斯贝 ksb 
233221100   梅德福 mdf 
233221200   塞勒姆 slm 
233221300   圣海伦斯    shls    
233221400   斯普林菲尔德  splfed  
233221500   尤金  yj  
233230000   佛罗里达    flld    
233230100   奥兰多 ald 
233230200   基韦斯特    jwst    
233230300   杰克逊维尔   jkxwe   
233230400   卡纳维尔角   knwej   
233230500   罗德岱堡    lddb    
233230600   迈阿密 mam 
233230700   圣彼德斯堡市  sbdsbs  
233230800   塔拉哈西    tlhx    
233230900   坦帕  tp  
233240000   佛蒙特 fmt 
233240100   伯灵顿 bld 
233240200   拉特兰 ltl 
233240300   南伯灵顿    nbld    
233250000   哥伦比亚特区  glbytq  
233250100   华盛顿哥伦比亚特区   hsdglbytq   
233260000   华盛顿 hsd 
233260100   斯波坎 sbk 
233260200   塔科马 tkm 
233260300   西雅图 xyt 
233270000   怀俄明 hem 
233270100   埃文斯顿    awsd    
233270200   卡斯珀 ksp 
233270300   拉勒米 llm 
233270400   罗克斯普林斯  lkspls  
233270500   夏延  xy  
233270600   谢里登 xld 
233280000   加利福尼亚   jlfny   
233280100   旧金山 jjs 
233280200   洛杉矶 lsj 
233280300   圣迭戈 sdg 
233280400   圣何塞 shs 
233290000   堪萨斯 kss 
233290100   阿比林 abl 
233290200   奥弗兰公园   aflgy   
233290300   哈钦森 hqs 
233290400   堪萨斯城    kssc    
233290500   莱文沃思    lwws    
233290600   劳伦斯 lls 
233290700   曼哈顿 mhd 
233290800   托皮卡 tpk 
233290900   威奇托 wqt 
233300000   康涅狄格    kndg    
233300100   布里奇波特   blqbt   
233300200   达里恩 dle 
233300300   格林尼治    glnz    
233300400   哈特福德    htfd    
233300500   米德尔顿    mded    
233300600   纽黑文 nhw 
233300700   韦斯特波特   wstbt   
233300800   沃特伯里    wtbl    
233300900   新不列颠    xbld    
233310000   科罗拉多    klld    
233310100   阿斯彭 asp 
233310200   奥罗拉 all 
233310300   博尔德 bed 
233310400   大章克申    dzks    
233310500   丹佛  df  
233310600   柯林斯堡    klsb    
233310700   科罗拉多斯普林斯    klldspls    
233310800   韦尔  we  
233320000   肯塔基 ktj 
233320100   列克星敦    lkxd    
233320200   路易斯维尔   lyswe   
233320300   欧文斯伯勒   owsbl   
233330000   路易斯安那   lysan   
233330100   巴吞鲁日    btlr    
233330200   什里夫波特   slfbt   
233330300   新奥尔良    xael    
233340000   罗德岛 ldd 
233340100   波塔基特    btjt    
233340200   克兰斯顿    klsd    
233340300   纽波特 nbt 
233340400   普罗维登斯   plwds   
233340500   韦斯特利    wstl    
233340600   文索基特    wsjt    
233340700   沃威克 wwk 
233350000   马里兰 mll 
233350100   巴尔的摩    bedm    
233350200   盖瑟斯堡    gssb    
233350300   罗克维尔    lkwe    
233360000   马萨诸塞    mszs    
233360100   波士顿 bsd 
233360200   斯普林菲尔德  splfed  
233360300   伍斯特 wst 
233370000   蒙大拿 mdn 
233370100   比灵斯 bls 
233370200   大瀑布村    dpbc    
233370300   米苏拉 msl 
233380000   密苏里 msl 
233380100   哥伦比亚    glby    
233380200   杰佛逊市    jfxs    
233380300   堪萨斯城    kssc    
233380400   圣路易斯    slys    
233380500   斯普林菲尔德  splfed  
233390000   密西西比    mxxb    
233390100   比洛克西    blkx    
233390200   格尔夫波特   gefbt   
233390300   格林维尔    glwe    
233390400   哈蒂斯堡    hdsb    
233390500   杰克逊 jkx 
233390600   默里迪恩    mlde    
233390700   维克斯堡    wksb    
233400000   密歇根 mxg 
233400100   安娜堡 anb 
233400200   巴特尔克里克  bteklk  
233400300   贝城  bc  
233400400   大急流城    djlc    
233400500   迪尔伯恩    debe    
233400600   底特律 dtl 
233400700   弗林特 flt 
233400800   怀恩多特    hedt    
233400900   卡拉马袓    klmj    
233401000   兰辛  lx  
233401100   马斯基根    msjg    
233401200   庞菷亚克    pzyk    
233401300   萨吉诺 sjn 
233401400   苏圣玛丽    ssml    
233401500   沃伦  wl  
233401600   休伦港 xlg 
233410000   缅因  my  
233410100   班戈  bg  
233410200   波特兰 btl 
233410300   刘易斯顿    lysd    
233420000   明尼苏达    mnsd    
233420100   罗切斯特    lqst    
233420200   明尼阿波利斯  mnabls  
233420300   圣保罗 sbl 
233430000   南达科他    ndkt    
233430100   阿伯丁 abd 
233430200   拉皮德城    lpdc    
233430300   苏福尔斯    sfes    
233440000   南卡罗来纳   nklln   
233440100   北查尔斯顿   bcesd   
233440200   查尔斯顿    cesd    
233440300   哥伦比亚    glby    
233450000   内布拉斯加   nblsj   
233450100   奥马哈 amh 
233450200   贝尔维尤    bewy    
233450300   林肯  lk  
233460000   内华达 nhd 
233460100   埃尔科 aek 
233460200   北拉斯维加斯  blswjs  
233460300   弗吉尼亚城   fjnyc   
233460400   亨德森 hds 
233460500   卡森城 ksc 
233460600   拉斯维加斯   lswjs   
233460700   里诺  ln  
233460800   斯帕克斯    spks    
233470000   纽约  ny  
233470100   布法罗 bfl 
233470200   罗切斯特    lqst    
233470300   纽约市 nys 
233480000   特拉华 tlh 
233480100   多佛  df  
233480200   纽瓦克 nwk 
233480300   威明顿 wmd 
233490000   田纳西 tnx 
233490100   布利斯托    blst    
233490200   查塔努加    ctnj    
233490300   金斯波特    jsbt    
233490400   孟菲斯 mfs 
233490500   纳什维尔    nswe    
233490600   诺克斯维尔   nkswe   
233490700   三城区 scq 
233490800   士麦那 smn 
233490900   斯普林希尔   splxe   
233491000   约翰逊城    yhxc    
233500000   威斯康星    wskx    
233500100   阿普尓顿    aped    
233500200   奥什科什    asks    
233500300   格林贝 glb 
233500400   基诺沙 jns 
233500500   拉克罗斯    lkls    
233500600   拉辛  lx  
233500700   马尼托沃克   mntwk   
233500800   迈迪逊 mdx 
233500900   密尔沃基    mewj    
233501000   欧克莱尓    okle    
233501100   沃索  ws  
233501200   希博伊根    xbyg    
233510000   维吉尼亚    wjny    
233510100   弗吉尼亚比奇  fjnybq  
233510200   诺福克 nfk 
233510300   切萨皮克    qspk    
233520000   西佛吉尼亚   xfjny   
233520100   查尔斯顿    cesd    
233520200   亨廷顿 htd 
233520300   帕克斯堡    pksb    
233530000   夏威夷 xwy 
233530100   凯卢阿 kla 
233530200   檀香山 txs 
233530300   希洛  xl  
233540000   新罕布什尔   xhbse   
233540100   康科德 kkd 
233540200   曼彻斯特    mcst    
233540300   纳舒厄 nse 
233550000   新墨西哥    xmxg    
233550100   阿尔伯克基   aebkj   
233550200   拉斯克鲁塞斯  lsklss  
233550300   罗斯韦尔    lswe    
233550400   圣菲  sf  
233560000   新泽西 xzx 
233560100   纽瓦克 nwk 
233560200   帕特森 pts 
233560300   泽西城 zxc 
233570000   亚利桑那    ylsn    
233570100   凤凰城 fhc 
233570200   格兰代尔    glde    
233570300   梅萨  ms  
233570400   史卡兹代尔   skzde   
233570500   坦普  tp  
233570600   图森  ts  
233570700   优玛  ym  
233580000   伊利诺斯    ylns    
233580100   奥尔顿 aed 
233580200   奥罗拉 all 
233580300   布卢明顿    blmd    
233580400   丹维尓 dwe 
233580500   迪卡尔布    dkeb    
233580600   迪凯持 dkc 
233580700   东圣路易斯   dslys   
233580800   厄巴纳-香槟  ebn-xb  
233580900   盖尔斯堡    gesb    
233581000   卡本代尔    kbde    
233581100   罗克艾兰    lkal    
233581200   罗克福德    lkfd    
233581300   诺黙尔 nme 
233581400   皮奥里亚    paly    
233581500   森特勒利亚   stlly   
233581600   斯普林菲尔德  splfed  
233581700   沃其根 wqg 
233581800   芝加哥 zjg 
233590000   印第安那    ydan    
233590100   埃文斯维尔   awswe   
233590200   韦恩堡 web 
233590300   印第安纳波利斯 ydanbls 
233600000   犹他  yt  
233600100   奥格登 agd 
233600200   雷登  ld  
233600300   欧仁  or  
233600400   帕克城 pkc 
233600500   普罗沃 plw 
233600600   圣乔治 sqz 
233600700   西瓦利城    xwlc    
233600800   盐湖城 yhc 
233610000   佐治亚 zzy 
233610100   奥古斯塔    agst    
233610200   哥伦布 glb 
233610300   梅肯  mk  
233610400   沙瓦纳 swn 
233610500   亚特兰大    ytld    
234000000   美属萨摩亚   mssmy   
234110000   阿纳  an  
234120000   阿图阿 ata 
234130000   艾加伊勒泰   ajylt   
234140000   法塞莱莱阿加  fsllaj  
234150000   加盖福毛加   jgfmj   
234160000   加加埃毛加   jjamj   
234170000   帕劳利 pll 
234180000   萨图帕伊泰阿  stpyta  
234190000   萨瓦伊岛    swyd    
234200000   图阿马萨加   tamsj   
234210000   瓦奥福诺蒂   wafnd   
234220000   韦西加诺    wxjn    
234230000   乌波卢岛    wbld    
235000000   美属外岛    mswd    
236000000   蒙古  mg  
236110000   巴彦洪格尔   byhge   
236120000   巴彦乌勒盖   bywlg   
236130000   布尔干 beg 
236140000   达尔汗乌勒   dehwl   
236150000   东方  df  
236160000   东戈壁 dgb 
236170000   鄂尔浑 eeh 
236180000   戈壁阿尔泰   gbaet   
236190000   戈壁苏木贝尔  gbsmbe  
236200000   后杭爱 hha 
236210000   科布多 kbd 
236220000   肯特  kt  
236230000   库苏古尔    ksge    
236240000   南戈壁 ngb 
236250000   前杭爱 qha 
236260000   色楞格 slg 
236270000   苏赫巴托尔   shbte   
236280000   乌布苏 wbs 
236290000   乌兰巴托市   wlbts   
236300000   扎布汗 zbh 
236310000   中戈壁 zgb 
236320000   中央  zy  
237000000   蒙特塞拉特   mtslt   
238000000   孟加拉 mjl 
238110000   达卡  dk  
238120000   吉大港 jdg 
238130000   库尔纳 ken 
239000000   密克罗尼西亚  mklnxy  
240000000   秘鲁  ml  
240110000   阿雷基帕    aljp    
240120000   阿普里马克   aplmk   
240130000   阿亚库乔    aykq    
240140000   安卡什 aks 
240150000   胡利亚卡    hlyk    
240160000   胡宁  hn  
240170000   卡哈马卡    khmk    
240180000   卡亚俄 kye 
240190000   库斯科 ksk 
240200000   拉利伯塔德   llbtd   
240210000   兰巴耶克    lbyk    
240220000   利马  lm  
240230000   洛雷托 llt 
240240000   马德雷德迪奥斯 mdlddas 
240250000   莫克瓜 mkg 
240260000   帕斯科 psk 
240270000   皮乌拉 pwl 
240280000   普诺  pn  
240290000   钦博特 qbt 
240300000   钦查阿尔塔   qcaet   
240310000   圣马丁 smd 
240320000   苏拉纳 sln 
240330000   塔克纳 tkn 
240340000   通贝斯 tbs 
240350000   瓦努科 wnk 
240360000   万卡维利卡   wkwlk   
240370000   乌卡亚利    wkyl    
240380000   亚马孙 yms 
240390000   伊卡  yk  
241000000   缅甸  md  
241110000   勃固省 bgs 
241120000   掸邦  db  
241130000   德林达依省   dldys   
241140000   克伦邦 klb 
241150000   克钦邦 kqb 
241160000   克耶邦 kyb 
241170000   马圭省 mgs 
241180000   曼德勒省    mdls    
241190000   孟邦  mb  
241200000   钦邦  qb  
241210000   若开邦 rkb 
241220000   实皆省 sjs 
241230000   仰光省 ygs 
241240000   伊洛瓦底省   ylwds   
242000000   摩尔多瓦    medw    
243000000   摩洛哥 mlg 
243110000   丹吉尔 dje 
243120000   得土安 dta 
243130000   非斯  fs  
243140000   卡萨布兰卡   ksblk   
243150000   拉巴特 lbt 
243160000   马拉喀什    mlks    
243170000   梅克内斯    mkns    
243180000   乌季达 wjd 
243190000   西撒哈拉    xshl    
244000000   摩纳哥 mng 
245000000   莫桑比克    msbk    
246000000   墨西哥 mxg 
246110000   阿瓜斯卡连斯特 agsklst 
246120000   阿卡普尔科   akpek   
246130000   埃莫西约    amxy    
246140000   埃佩切 apq 
246150000   奥夫雷贡城   aflgc   
246160000   奥里萨巴    alsb    
246170000   巴利城 blc 
246180000   巴亚尔塔港   byetg   
246190000   比利亚埃尔莫萨 blyaems 
246200000   波萨里卡    bslk    
246210000   蒂华纳 dhn 
246220000   杜兰戈 dlg 
246230000   恩塞纳达    esnd    
246240000   瓜达拉哈拉   gdlhl   
246250000   瓜纳华托    gnht    
246260000   哈拉帕 hlp 
246270000   华雷斯 hls 
246280000   华雷斯港    hlsg    
246290000   卡门  km  
246300000   科利马 klm 
246310000   克雷塔罗    kltl    
246320000   库埃纳瓦卡   kanwk   
246330000   库利阿坎    klak    
246340000   夸察夸拉克斯  kcklks  
246350000   拉巴斯 lbs 
246360000   莱昂  la  
246370000   雷诺萨 lns 
246380000   洛斯莫奇斯   lsmqs   
246390000   马萨特兰    mstl    
246400000   马塔莫罗斯   mtmls   
246410000   梅里达 mld 
246420000   蒙克洛瓦    mklw    
246430000   蒙特雷 mtl 
246440000   莫雷利亚    mlly    
246450000   墨西哥城    mxgc    
246460000   墨西卡利    mxkl    
246470000   诺加莱斯    njls    
246480000   帕丘卡 pqk 
246490000   普埃布拉    pabl    
246500000   奇尔潘辛戈   qepxg   
246510000   奇瓦瓦 qww 
246520000   切图马尔    qtme    
246530000   萨尔蒂约    sedy    
246540000   萨卡特卡斯   sktks   
246550000   塞拉亚 sly 
246560000   圣路易斯波托亚 slysbty 
246570000   塔帕丘拉    tpql    
246580000   坦皮科 tpk 
246590000   特拉斯卡拉   tlskl   
246600000   特皮克 tpk 
246610000   特瓦坎 twk 
246620000   图斯特拉-古铁雷斯   tstl-gtls   
246630000   托雷翁 tlw 
246640000   托卢卡 tlk 
246650000   瓦哈卡 whk 
246660000   维多利亚城   wdlyc   
246670000   韦拉克鲁斯   wlkls   
246680000   乌鲁阿潘    wlap    
246690000   新拉雷多    xlld    
246700000   伊拉普阿托   ylpat   
247000000   纳米比亚    nmby    
247110000   埃龙戈 alg 
247120000   奥汉圭纳    ahgn    
247130000   奥卡万戈    akwg    
247140000   奥马赫科    amhk    
247150000   奥姆沙蒂    amsd    
247160000   奥乔宗蒂约巴  aqzdyb  
247170000   奥沙纳 asn 
247180000   奥希科托    axkt    
247190000   哈达普 hdp 
247200000   霍马斯 hms 
247210000   卡拉斯 kls 
247220000   卡普里维    kplw    
247230000   库内内 knn 
248000000   南非  nf  
248110000   阿平顿 apd 
248120000   艾利弗山    alfs    
248130000   彼德马里茨堡  bdmlcb  
248140000   彼德斯堡    bdsb    
248150000   比勒陀利亚   bltly   
248160000   比索  bs  
248170000   布雷达斯多普  bldsdp  
248180000   布隆方丹    blfd    
248190000   布隆克斯特斯普利特   blkstsplt   
248200000   德阿尔 dae 
248210000   德班  db  
248220000   邓迪  dd  
248230000   东巴克利    dbkl    
248240000   东伦敦 dld 
248250000   弗雷堡 flb 
248260000   弗里尼欣    flnx    
248270000   格罗布莱斯达尔 glblsde 
248280000   基雅尼 jyn 
248290000   金伯利 jbl 
248300000   开普敦 kpd 
248310000   克莱克斯多普  klksdp  
248320000   库鲁曼 klm 
248330000   昆士敦 ksd 
248340000   莱迪史密斯   ldsms   
248350000   兰德方丹    ldfd    
248360000   理查兹湾    lczw    
248370000   利斯滕堡    lstb    
248380000   米德尔堡    mdeb    
248390000   姆库泽 mkz 
248400000   穆里斯堡    mlsb    
248410000   内尔斯普雷特  nesplt  
248420000   尼尔斯特隆   nestl   
248430000   纽卡斯尔    nkse    
248440000   乔治  qz  
248450000   萨索尔堡    sseb    
248460000   瑟孔达 skd 
248470000   特克索波    tksb    
248480000   特隆普斯堡   tlpsb   
248490000   跳羚  tl  
248500000   图拉马哈谢   tlmhx   
248510000   托霍延杜    thyd    
248520000   韦茨肖克    wcxk    
248530000   韦尔科姆    wekm    
248540000   乌伦迪 wld 
248550000   乌姆塔塔    wmtt    
248560000   伍斯特 wst 
248570000   西博福特    xbft    
248580000   谢普斯通港   xpstg   
248590000   伊丽莎白港   ylsbg   
248600000   约翰内斯堡   yhnsb   
249000000   南极洲 njz 
250000000   南乔治亚和南桑德威奇群岛    nqzyhnsdwqqd    
251000000   瑙鲁  nl  
252000000   尼泊尔 nbe 
252110000   巴格马蒂    bgmd    
252120000   道拉吉里    dljl    
252130000   甘达基 gdj 
252140000   戈西  gx  
252150000   格尔纳利    genl    
252160000   贾纳克布尔   jnkbe   
252170000   拉布蒂 lbd 
252180000   蓝毗尼 lpn 
252190000   马哈卡利    mhkl    
252200000   梅吉  mj  
252210000   纳拉亚尼    nlyn    
252220000   佩里  pl  
252230000   萨加玛塔    sjmt    
252240000   塞蒂  sd  
253000000   尼加拉瓜    njlg    
253110000   埃斯特利    astl    
253120000   北大西洋    bdxy    
253130000   博阿科 bak 
253140000   格拉纳达    glnd    
253150000   卡拉索 kls 
253160000   莱昂  la  
253170000   里瓦斯 lws 
253180000   马德里斯    mdls    
253190000   马那瓜 mng 
253200000   马萨亚 msy 
253210000   马塔加尔帕   mtjep   
253220000   南大西洋    ndxy    
253230000   奇南德加    qndj    
253240000   琼塔莱斯    qtls    
253250000   圣胡安河    shah    
253260000   希诺特加    xntj    
253270000   新塞哥维亚   xsgwy   
254000000   尼日尔 nre 
254110000   阿加德兹    ajdz    
254120000   迪法  df  
254130000   蒂拉贝里    dlbl    
254140000   多索  ds  
254150000   津德尔 jde 
254160000   马拉迪 mld 
254170000   尼亚美市    nyms    
254180000   塔瓦  tw  
255000000   尼日利亚    nrly    
255110000   阿比亚 aby 
255120000   奥博莫绍    abms    
255130000   卡诺  kn  
255140000   拉各斯 lgs 
255150000   伊巴丹 ybd 
256000000   纽埃  na  
257000000   挪威  nw  
257110000   阿克什胡斯   akshs   
257120000   奥普兰 apl 
257130000   奥斯陆市    asls    
257140000   北特伦德拉格  btldlg  
257150000   布斯克吕    bskl    
257160000   东阿格德尔   dagde   
257170000   东福尔 dfe 
257180000   芬马克 fmk 
257190000   海德马克    hdmk    
257200000   霍达兰 hdl 
257210000   罗加兰 ljl 
257220000   默勒－鲁姆斯达尔    ml－lmsde    
257230000   南特伦德拉格  ntldlg  
257240000   诺尔兰 nel 
257250000   松恩－菲尤拉讷 se－fyln 
257260000   泰勒马克    tlmk    
257270000   特罗姆斯    tlms    
257280000   西阿格德尔   xagde   
257290000   西福尔 xfe 
258000000   诺福克 nfk 
259000000   帕劳群岛    plqd    
260000000   皮特凯恩    ptke    
261000000   葡萄牙 pty 
261110000   滨海阿连特茹  bhaltr  
261120000   滨海皮尼亚尔  bhpnye  
261130000   波尔图 bet 
261140000   杜罗  dl  
261150000   恩特拉杜罗伏日 etldlfr 
261160000   法鲁  fl  
261170000   丰沙尔 fse 
261180000   卡瓦多 kwd 
261190000   科瓦贝拉    kwbl    
261200000   里斯本 lsb 
261210000   利巴特茹    lbtr    
261220000   梅地奥特茹   mdatr   
261230000   米尼奥-利马  mna-lm  
261240000   内贝拉北    nblb    
261250000   内贝拉南    nbln    
261260000   内皮尼亚尔北  npnyeb  
261270000   内皮尼亚尔南  npnyen  
261280000   蓬塔德尔加达  ptdejd  
261290000   塞图巴尔半岛  stbebd  
261300000   山后  sh  
261310000   上阿连特茹   saltr   
261320000   上特拉斯山   stlss   
261330000   塔梅加 tmj 
261340000   万福  wf  
261350000   西部  xb  
261360000   下阿连特茹   xaltr   
261370000   下伏日 xfr 
261380000   下蒙德古    xmdg    
261390000   中阿连特茹   zaltr   
262000000   乔治亚 qzy 
263000000   日本  rb  
263110000   爱媛  ay  
263120000   爱知  az  
263130000   北海道 bhd 
263140000   兵库  bk  
263150000   冲绳  cs  
263160000   茨城  cc  
263170000   大阪  db  
263180000   大分  df  
263190000   岛根  dg  
263200000   徳岛  dd  
263210000   东京  dj  
263220000   福岛  fd  
263230000   福冈  fg  
263240000   福井  fj  
263250000   富山  fs  
263260000   冈山  gs  
263270000   高知  gz  
263280000   宮城  gc  
263290000   宫崎  gq  
263300000   广岛  gd  
263310000   和歌山 hgs 
263320000   京都  jd  
263330000   静冈  jg  
263340000   枥木  lm  
263350000   鹿儿岛 led 
263360000   奈良  nl  
263370000   鸟取  nq  
263380000   岐阜  qf  
263390000   埼玉  qy  
263400000   千叶  qy  
263410000   青森  qs  
263420000   秋田  qt  
263430000   群马  qm  
263440000   三重  sz  
263450000   山口  sk  
263460000   山梨  sl  
263470000   山形  sx  
263480000   神奈川 snc 
263490000   石川  sc  
263500000   香川  xc  
263510000   新潟  xx  
263520000   熊本  xb  
263530000   岩手  ys  
263540000   长崎  zq  
263550000   长野  zy  
263560000   滋贺  zh  
263570000   佐贺  zh  
264000000   瑞典  rd  
264110000   北博滕 bbt 
264120000   布莱金厄    blje    
264130000   达拉纳 dln 
264140000   东约特兰    dytl    
264150000   厄勒布鲁    elbl    
264160000   哥得兰 gdl 
264170000   哈兰  hl  
264180000   卡尔马 kem 
264190000   克鲁努贝里   klnbl   
264200000   南曼兰 nml 
264210000   斯德哥尔摩   sdgem   
264220000   斯科耐 skn 
264230000   韦姆兰 wml 
264240000   乌普萨拉    wpsl    
264250000   西博滕 xbt 
264260000   西曼兰 xml 
264270000   西诺尔兰    xnel    
264280000   西约特兰    xytl    
264290000   延雪平 yxp 
264300000   耶夫勒堡    yflb    
264310000   耶姆特兰    ymtl    
265000000   瑞士  rs  
265110000   阿尔高 aeg 
265120000   巴塞尔城市   bsecs   
265130000   巴塞尔乡村   bsexc   
265140000   伯尔尼 ben 
265150000   楚格  cg  
265160000   弗里堡 flb 
265170000   格拉鲁斯    glls    
265180000   格劳宾登    glbd    
265190000   卢塞恩 lse 
265200000   洛桑  ls  
265210000   纳沙泰尔    nste    
265220000   内阿彭策尔   napce   
265230000   日内瓦 rnw 
265240000   汝拉  rl  
265250000   沙夫豪森    sfhs    
265260000   上瓦尔登    swed    
265270000   圣加仑 sjl 
265280000   施维茨 swc 
265290000   苏黎世 sls 
265300000   索洛图恩    slte    
265310000   提契诺 tqn 
265320000   图尔高 teg 
265330000   瓦莱  wl  
265340000   外阿彭策尔   wapce   
265350000   沃   w   
265360000   乌里  wl  
265370000   下瓦尔登    xwed    
266000000   萨尔瓦多    sewd    
266110000   阿波帕 abp 
266120000   阿瓦查潘    awcp    
266130000   滨海  bh  
266140000   查拉特南戈   cltng   
266150000   德尔加多    dejd    
266160000   基埃-恩特姆  ja-etm  
266170000   卡瓦尼亚斯   kwnys   
266180000   库斯卡特兰   ksktl   
266190000   拉巴斯 lbs 
266200000   拉利伯塔德   llbtd   
266210000   拉乌尼翁    lwnw    
266220000   梅基卡诺斯   mjkns   
266230000   莫拉桑 mls 
266240000   圣安娜 san 
266250000   圣米格尔    smge    
266260000   圣萨尔瓦多   ssewd   
266270000   圣维森特    swst    
266280000   松索纳特    ssnt    
266290000   索亚潘戈    sypg    
266300000   韦莱-恩萨斯  wl-ess  
266310000   乌苏卢坦    wslt    
266320000   伊洛潘戈    ylpg    
266330000   中南  zn  
267000000   萨摩亚 smy 
268000000   塞尔维亚,黑山 sewy,hs 
268110000   贝尔格莱德   begld   
268120000   波德戈里察   bdglc   
268130000   克拉古涅瓦茨  klgnwc  
268140000   尼什  ns  
268150000   诺维萨德    nwsd    
268160000   普里什蒂纳   plsdn   
268170000   苏博蒂察    sbdc    
268180000   泽蒙  zm  
269000000   塞拉利昂    slla    
269110000   北部  bb  
269120000   东部  db  
269130000   南部  nb  
269140000   西部区 xbq 
270000000   塞内加尔    snje    
270110000   达喀尔 dke 
270120000   法蒂克 fdk 
270130000   济金绍尔    jjse    
270140000   捷斯  js  
270150000   久尔贝勒    jebl    
270160000   考拉克 klk 
270170000   科尔达 ked 
270180000   卢加  lj  
270190000   马塔姆 mtm 
270200000   圣路易 sly 
270210000   坦巴昆达    tbkd    
271000000   塞浦路斯    spls    
271110000   法马古斯塔   fmgst   
271120000   凯里尼亚    klny    
271130000   拉纳卡 lnk 
271140000   利马索尔    lmse    
271150000   尼科西亚    nkxy    
271160000   帕福斯 pfs 
272000000   塞舌尔 sse 
273000000   沙特阿拉伯   stalb   
273110000   阿尔阿尔    aeae    
273120000   艾卜哈 abh 
273130000   巴哈  bh  
273140000   布赖代 bld 
273150000   达曼  dm  
273160000   哈费尔巴廷   hfebt   
273170000   哈伊勒 hyl 
273180000   海米斯穆谢特  hmsmxt  
273190000   海耶  hy  
273200000   胡富夫 hff 
273210000   吉达  jd  
273220000   吉赞  jz  
273230000   利雅得 lyd 
273240000   麦地那 mdn 
273250000   麦加  mj  
273260000   姆巴拉兹    mblz    
273270000   纳季兰 njl 
273280000   塞卡卡 skk 
273290000   塔布克 tbk 
273300000   塔伊夫 tyf 
273310000   延布  yb  
273320000   朱拜勒 zbl 
274000000   圣诞岛 sdd 
275000000   圣多美和普林西比    sdmhplxb    
276000000   圣赫勒拿    shln    
277000000   圣基茨和尼维斯 sjchnws 
278000000   圣卢西亚    slxy    
279000000   圣马力诺    smln    
280000000   圣皮埃尔和米克隆群岛  spaehmklqd  
281000000   圣文森特和格林纳丁斯  swsthglnds  
282000000   斯里兰卡    sllk    
282110000   阿努拉德普勒  anldpl  
282120000   安帕赖 apl 
282130000   巴杜勒 bdl 
282140000   拜蒂克洛    bdkl    
282150000   波隆纳鲁沃   blnlw   
282160000   汉班托特    hbtt    
282170000   基里诺奇    jlnq    
282180000   加勒  jl  
282190000   加姆珀哈    jmph    
282200000   贾夫纳 jfn 
282210000   卡卢特勒    kltl    
282220000   凯格勒 kgl 
282230000   康提  kt  
282240000   科伦坡 klp 
282250000   库鲁内格勒   klngl   
282260000   拉特纳普勒   ltnpl   
282270000   马纳尔 mne 
282280000   马特莱 mtl 
282290000   马特勒 mtl 
282300000   莫讷勒格勒   mnlgl   
282310000   穆莱蒂武    mldw    
282320000   努沃勒埃利耶  nwlaly  
282330000   普塔勒姆    ptlm    
282340000   亭可马里    tkml    
282350000   瓦武尼亚    wwny    
283000000   斯洛伐克    slfk    
283110000   班斯卡-比斯特里察   bsk-bstlc   
283120000   布拉迪斯拉发  bldslf  
283130000   科希策 kxc 
283140000   尼特拉 ntl 
283150000   普雷绍夫    plsf    
283160000   日利纳 rln 
283170000   特尔纳瓦    tenw    
283180000   特伦钦 tlq 
284000000   斯洛文尼亚   slwny   
284110000   奥巴尔诺-克拉 aben-kl 
284120000   奥斯雷德涅斯洛文    asldnslw    
284130000   波德拉夫    bdlf    
284140000   波穆尔 bme 
284150000   多雷尼 dln 
284160000   戈雷尼 gln 
284170000   戈里  gl  
284180000   科洛  kl  
284190000   诺特拉尼    ntln    
284200000   萨维尼 swn 
284210000   斯波德涅波萨夫 sbdnbsf 
284220000   扎萨夫 zsf 
285000000   斯瓦尔巴和扬马廷    swebhymt    
286000000   斯威士兰    swsl    
287000000   苏丹  sd  
287110000   北部  bb  
287120000   赤道  cd  
287130000   达尔富尔    defe    
287140000   东部  db  
287150000   加扎勒河    jzlh    
287160000   喀土穆 ktm 
287170000   科尔多凡    kedf    
287180000   上尼罗 snl 
287190000   中部  zb  
288000000   苏里南 sln 
288110000   布罗科蓬多   blkpd   
288120000   科罗尼 kln 
288130000   科默韦讷    kmwn    
288140000   马罗韦讷    mlwn    
288150000   尼克里 nkl 
288160000   帕拉  pl  
288170000   帕拉马里博   plmlb   
288180000   萨拉马卡    slmk    
288190000   瓦尼卡 wnk 
288200000   西帕里韦尼   xplwn   
289000000   所罗门群岛   slmqd   
289110000   瓜达尔卡纳尔  gdekne  
289120000   霍尼亚拉    hnyl    
289130000   拉纳尔和贝罗纳 lnehbln 
289140000   马基拉 mjl 
289150000   马莱塔 mlt 
289160000   乔伊索 qys 
289170000   泰莫图 tmt 
289180000   西部  xb  
289190000   伊萨贝尔    ysbe    
289200000   中部群岛    zbqd    
290000000   索马里 sml 
291000000   塔吉克斯坦   tjkst   
291110000   杜尚别 dsb 
291120000   霍罗格 hlg 
291130000   卡尼巴达姆   knbdm   
291140000   科法尔尼洪   kfenh   
291150000   苦盏  kz  
291160000   库尔干-秋别  keg-qb  
291170000   库洛布 klb 
291180000   洛贡  lg  
291190000   努雷克 nlk 
291200000   彭吉肯特    pjkt    
291210000   萨班特 sbt 
291220000   塔博沙尔    tbse    
291230000   图尔孙扎德   teszd   
291240000   乌拉秋别    wlqb    
291250000   伊斯法拉    ysfl    
292000000   泰国  tg  
292110000   安纳乍能    anzn    
292120000   巴蜀  bs  
292130000   巴吞他尼    bttn    
292140000   巴真  bz  
292150000   北碧  bb  
292160000   北标  bb  
292170000   北大年 bdn 
292180000   北揽  bl  
292190000   北榄坡 blp 
292200000   北柳  bl  
292210000   碧差汶 bcw 
292220000   博达伦 bdl 
292230000   猜那  cn  
292240000   猜也奔 cyb 
292250000   程逸  cy  
292260000   春蓬  cp  
292270000   春武里 cwl 
292280000   达   d   
292290000   达叻  dl  
292300000   大城  dc  
292310000   董里  dl  
292320000   佛丕  fp  
292330000   佛统  ft  
292340000   甘烹碧 gpb 
292350000   红统  ht  
292360000   华富里 hfl 
292370000   加拉信 jlx 
292380000   甲米  jm  
292390000   尖竹汶 jzw 
292400000   孔敬  kj  
292410000   拉农  ln  
292420000   廊开  lk  
292430000   廊莫那浦    lmnp    
292440000   叻丕  lp  
292450000   黎   l   
292460000   黎逸  ly  
292470000   龙仔厝 lzc 
292480000   罗勇  ly  
292490000   洛坤  lk  
292500000   玛哈沙拉堪   mhslk   
292510000   曼谷  mg  
292520000   莫达汉 mdh 
292530000   那空那育    nkny    
292540000   那空帕农    nkpn    
292550000   难   n   
292560000   南奔  nb  
292570000   暖武里 nwl 
292580000   帕   p   
292590000   帕尧  py  
292600000   攀牙  py  
292610000   彭世洛 psl 
292620000   披集  pj  
292630000   普吉  pj  
292640000   清莱  ql  
292650000   清迈  qm  
292660000   色军  sj  
292670000   沙敦  sd  
292680000   沙缴  sj  
292690000   四色菊 ssj 
292700000   宋卡  sk  
292710000   素可泰 skt 
292720000   素叻  sl  
292730000   素林  sl  
292740000   素攀武里    spwl    
292750000   陶公  tg  
292760000   乌隆  wl  
292770000   乌泰他尼    wttn    
292780000   乌汶  ww  
292790000   武里南 wln 
292800000   信武里 xwl 
292810000   耶梭通 yst 
292820000   也拉  yl  
292830000   夜丰颂 yfs 
292840000   夜功  yg  
293000000   坦桑尼亚    tsny    
293110000   阿鲁沙 als 
293120000   奔巴北 bbb 
293130000   奔巴南 bbn 
293140000   滨海  bh  
293150000   达累斯萨拉姆  dlsslm  
293160000   多多马 ddm 
293170000   基戈马 jgm 
293180000   卡盖拉 kgl 
293190000   林迪  ld  
293200000   鲁夸  lk  
293210000   鲁伍马 lwm 
293220000   马腊  ml  
293230000   曼亚拉 myl 
293240000   莫洛戈罗    mlgl    
293250000   姆贝亚 mby 
293260000   姆特瓦拉    mtwl    
293270000   姆万扎 mwz 
293280000   乞力马扎罗   qlmzl   
293290000   桑给巴尔    sjbe    
293300000   桑给巴尔北   sjbeb   
293310000   桑给巴尔南   sjben   
293320000   桑给巴尔市和西 sjbeshx 
293330000   塔波拉 tbl 
293340000   坦噶  tg  
293350000   辛吉达 xjd 
293360000   欣延加 xyj 
293370000   伊林加 ylj 
294000000   汤加  tj  
294110000   埃瓦  aw  
294120000   哈派  hp  
294130000   纽阿斯 nas 
294140000   汤加塔布    tjtb    
294150000   瓦瓦乌 www 
295000000   特克斯和凯克特斯群岛  tkshkktsqd  
296000000   特里斯坦达昆哈 tlstdkh 
297000000   特立尼达和多巴哥    tlndhdbg    
298000000   突尼斯 tns 
298110000   艾尔亚奈    aeyn    
298120000   巴杰  bj  
298130000   本阿鲁斯    bals    
298140000   比塞大 bsd 
298150000   吉比利 jbl 
298160000   加贝斯 jbs 
298170000   加夫萨 jfs 
298180000   坚杜拜 jdb 
298190000   卡夫  kf  
298200000   卡塞林 ksl 
298210000   凯鲁万 klw 
298220000   马赫迪耶    mhdy    
298230000   马努巴 mnb 
298240000   梅德宁 mdn 
298250000   莫纳斯提尔   mnste   
298260000   纳布勒 nbl 
298270000   斯法克斯    sfks    
298280000   苏塞  ss  
298290000   泰塔温 ttw 
298300000   突尼斯 tns 
298310000   托泽尔 tze 
298320000   西迪布济德   xdbjd   
298330000   锡勒亚奈    xlyn    
298340000   宰格万 zgw 
299000000   图瓦卢 twl 
300000000   土耳其 teq 
300110000   阿达纳 adn 
300120000   阿德亚曼    adym    
300130000   阿尔达罕    aedh    
300140000   阿尔特温    aetw    
300150000   阿菲永 afy 
300160000   阿克萨赖    aksl    
300170000   阿勒  al  
300180000   阿马西亚    amxy    
300190000   埃迪尔内    aden    
300200000   埃尔津詹    aejz    
300210000   埃尔祖鲁姆   aezlm   
300220000   埃拉泽 alz 
300230000   埃斯基谢希尔  asjxxe  
300240000   艾登  ad  
300250000   安卡拉 akl 
300260000   安塔利亚    atly    
300270000   奥尔杜 aed 
300280000   巴尔腾 bet 
300290000   巴勒克埃西尔  blkaxe  
300300000   巴特曼 btm 
300310000   巴伊布尔特   bybet   
300320000   比莱吉克    bljk    
300330000   比特利斯    btls    
300340000   宾格尔 bge 
300350000   博卢  bl  
300360000   布尔杜尔    bede    
300370000   布尔萨 bes 
300380000   昌克勒 ckl 
300390000   代尼兹利    dnzl    
300400000   迪亚巴克尔   dybke   
300410000   凡   f   
300420000   哈卡里 hkl 
300430000   哈塔伊 hty 
300440000   基利斯 jls 
300450000   吉雷松 jls 
300460000   加济安泰普   jjatp   
300470000   居米什哈内   jmshn   
300480000   卡尔斯 kes 
300490000   卡赫拉曼马拉什 khlmmls 
300500000   卡拉比克    klbk    
300510000   卡拉曼 klm 
300520000   卡斯塔莫努   kstmn   
300530000   开塞利 ksl 
300540000   科贾埃利    kjal    
300550000   柯克拉雷利   kklll   
300560000   科尼亚 kny 
300570000   克尔谢希尔   kexxe   
300580000   克勒克卡莱   klkkl   
300590000   拉飞  lf  
300600000   里泽  lz  
300610000   马尔丁 med 
300620000   马拉蒂亚    mldy    
300630000   马尼萨 mns 
300640000   穆拉  ml  
300650000   穆什  ms  
300660000   内夫谢希尔   nfxxe   
300670000   尼代  nd  
300680000   恰纳卡莱    qnkl    
300690000   乔鲁姆 qlm 
300700000   屈塔希亚    qtxy    
300710000   萨卡里亚    skly    
300720000   萨姆松 sms 
300730000   泰基尔达    tjed    
300740000   特拉布宗    tlbz    
300750000   通杰利 tjl 
300760000   托卡特 tkt 
300770000   乌萨克 wsk 
300780000   锡尔纳克    xenk    
300790000   锡尔特 xet 
300800000   锡诺普 xnp 
300810000   锡瓦斯 xws 
300820000   伊迪尔 yde 
300830000   伊切尔 yqe 
300840000   伊斯帕尔塔   yspet   
300850000   伊斯坦布尔   ystbe   
300860000   伊兹密尔    yzme    
300870000   约兹加特    yzjt    
300880000   宗古尔达克   zgedk   
301000000   土库曼斯坦   tkmst   
301110000   阿哈尔 ahe 
301120000   阿什哈巴德市  ashbds  
301130000   巴尔坎 bek 
301140000   达沙古兹    dsgz    
301150000   列巴普 lbp 
301160000   马雷  ml  
301170000   涅比特达格   nbtdg   
302000000   托克劳 tkl 
303000000   瓦利斯和福图纳 wlshftn 
304000000   瓦努阿图    wnat    
304110000   马朗帕 mlp 
304120000   彭纳马 pnm 
304130000   桑马  sm  
304140000   塔菲阿 tfa 
304150000   托尔巴 teb 
304160000   谢法  xf  
305000000   危地马拉    wdml    
305110000   埃尔普罗格雷索 aeplgls 
305120000   埃斯昆特拉   asktl   
305130000   哈拉帕 hlp 
305140000   胡蒂亚帕    hdyp    
305150000   基切  jq  
305160000   克萨尔特南戈  ksetng  
305170000   雷塔卢莱乌   ltllw   
305180000   米克斯科    mksk    
305190000   佩滕  pt  
305200000   奇基穆拉    qjml    
305210000   奇马尔特南戈  qmetng  
305220000   萨卡帕 skp 
305230000   萨卡特佩克斯  sktpks  
305240000   上韦拉帕斯   swlps   
305250000   圣罗莎 sls 
305260000   圣马科斯    smks    
305270000   苏奇特佩克斯  sqtpks  
305280000   索洛拉 sll 
305290000   托托尼卡潘   ttnkp   
305300000   危地马拉    wdml    
305310000   韦韦特南戈   wwtng   
305320000   下韦拉帕斯   xwlps   
305330000   新城  xc  
305340000   伊萨瓦尔    yswe    
306000000   维尔京群岛，美属    wejqd，ms    
307000000   维尔京群岛，英属    wejqd，ys    
308000000   委内瑞拉    wnrl    
308110000   阿拉瓜 alg 
308120000   阿马库罗三角洲 amklsjz 
308130000   阿普雷 apl 
308140000   安索阿特吉   asatj   
308150000   巴里纳斯    blns    
308160000   玻利瓦尔    blwe    
308170000   波图格萨    btgs    
308180000   法尔孔 fek 
308190000   瓜里科 glk 
308200000   加拉加斯    jljs    
308210000   卡拉沃沃    klww    
308220000   科赫德斯    khds    
308230000   拉腊  ll  
308240000   联邦属地    lbsd    
308250000   梅里达 mld 
308260000   米兰达 mld 
308270000   莫纳加斯    mnjs    
308280000   苏克雷 skl 
308290000   苏利亚 sly 
308300000   塔奇拉 tql 
308310000   特鲁希略    tlxl    
308320000   新埃斯帕塔   xaspt   
308330000   亚拉奎 ylk 
308340000   亚马孙 yms 
309000000   文莱  wl  
310000000   乌干达 wgd 
310110000   阿鲁阿 ala 
310120000   阿帕克 apk 
310130000   阿朱马尼    azmn    
310140000   本迪布焦    bdbj    
310150000   布吉里 bjl 
310160000   布西亚 bxy 
310170000   布谢尼 bxn 
310180000   恩通加莫    etjm    
310190000   古卢  gl  
310200000   霍伊马 hym 
310210000   基巴莱 jbl 
310220000   基博加 jbj 
310230000   基恩乔乔    jeqq    
310240000   基索罗 jsl 
310250000   基特古姆    jtgm    
310260000   金贾  jj  
310270000   卡巴莱 kbl 
310280000   卡巴罗莱    kbll    
310290000   卡贝拉马伊多  kblmyd  
310300000   卡兰加拉    kljl    
310310000   卡姆文盖    kmwg    
310320000   卡穆利 kml 
310330000   卡农古 kng 
310340000   卡普乔鲁瓦   kpqlw   
310350000   卡塞塞 kss 
310360000   卡塔奎 ktk 
310370000   卡永加 kyj 
310380000   坎帕拉 kpl 
310390000   科蒂多 kdd 
310400000   库米  km  
310410000   拉卡伊 lky 
310420000   利拉  ll  
310430000   卢韦罗 lwl 
310440000   鲁昆吉里    lkjl    
310450000   马萨卡 msk 
310460000   马辛迪 mxd 
310470000   马尤盖 myg 
310480000   莫罗托 mlt 
310490000   莫约  my  
310500000   姆巴拉拉    mbll    
310510000   姆巴莱 mbl 
310520000   姆皮吉 mpj 
310530000   穆本德 mbd 
310540000   穆科诺 mkn 
310550000   纳卡皮里皮里特 nkplplt 
310560000   纳卡松戈拉   nksgl   
310570000   内比  nb  
310580000   帕德尔 pde 
310590000   帕利萨 pls 
310600000   森巴布莱    sbbl    
310610000   索罗提 slt 
310620000   托罗罗 tll 
310630000   瓦基索 wjs 
310640000   锡龙科 xlk 
310650000   伊甘加 ygj 
310660000   永贝  yb  
311000000   乌克兰 wkl 
311110000   敖德萨 ads 
311120000   波尔塔瓦    betw    
311130000   第聂伯罗波得罗夫斯克  dnblbdlfsk  
311140000   顿涅茨克    dnck    
311150000   哈尔科夫    hekf    
311160000   赫尔松州    hesz    
311170000   赫梅利尼茨基  hmlncj  
311180000   基辅  jf  
311190000   基洛夫格勒   jlfgl   
311200000   捷尔诺波尔   jenbe   
311210000   克里米亚自治共和国   klmyzzghg   
311220000   利沃夫 lwf 
311230000   卢甘斯克    lgsk    
311240000   罗夫诺 lfn 
311250000   尼古拉耶夫   nglyf   
311260000   切尔卡瑟    qeks    
311270000   切尔尼戈夫   qengf   
311280000   切尔诺夫策   qenfc   
311290000   日托米尔    rtme    
311300000   苏梅  sm  
311310000   外喀尔巴阡   wkebq   
311320000   文尼察 wnc 
311330000   沃伦  wl  
311340000   伊万－弗兰科夫州    yw－flkfz    
311350000   扎波罗热    zblr    
312000000   乌拉圭 wlg 
312110000   阿蒂加斯    adjs    
312120000   杜拉斯诺    dlsn    
312130000   佛罗里达    flld    
312140000   弗洛雷斯    flls    
312150000   卡内洛内斯   knlns   
312160000   科洛尼亚    klny    
312170000   拉瓦耶哈    lwyh    
312180000   里韦拉 lwl 
312190000   罗恰  lq  
312200000   马尔多纳多   mednd   
312210000   蒙得维的亚   mdwdy   
312220000   内格罗河    nglh    
312230000   派桑杜 psd 
312240000   萨尔托 set 
312250000   塞罗拉尔戈   slleg   
312260000   三十三人    sssr    
312270000   圣何塞 shs 
312280000   索里亚诺    slyn    
312290000   塔夸伦博    tklb    
313000000   乌兹别克斯坦  wzbkst  
313110000   安集延 ajy 
313120000   布哈拉 bhl 
313130000   费尔干纳    fegn    
313140000   花拉子模    hlzm    
313150000   吉扎克 jzk 
313160000   卡拉卡尔帕克斯坦共和国 klkepkstghg 
313170000   卡什卡达里亚  kskdly  
313180000   纳曼干 nmg 
313190000   纳沃伊 nwy 
313200000   撒马尔罕    smeh    
313210000   苏尔汉河    sehh    
313220000   塔什干 tsg 
313230000   塔什干市    tsgs    
313240000   锡尔河 xeh 
314000000   西班牙 xby 
314110000   阿尔梅里亚   aemly   
314120000   阿尔瓦塞特   aewst   
314130000   阿拉瓦 alw 
314140000   阿利坎特    alkt    
314150000   阿斯图利亚斯  astlys  
314160000   阿维拉 awl 
314170000   奥伦塞 als 
314180000   巴达霍斯    bdhs    
314190000   巴利阿里    blal    
314200000   巴利亚多利德  blydld  
314210000   巴伦西亚    blxy    
314220000   巴塞罗那    bsln    
314230000   比斯开 bsk 
314240000   布尔戈斯    begs    
314250000   格拉纳达    glnd    
314260000   瓜达拉哈拉   gdlhl   
314270000   哈恩  he  
314280000   赫罗纳 hln 
314290000   吉普斯夸    jpsk    
314300000   加的斯 jds 
314310000   卡塞雷斯    ksls    
314320000   卡斯蒂利亚   ksdly   
314330000   卡斯特利翁   kstlw   
314340000   科尔多瓦    kedw    
314350000   昆卡  kk  
314360000   拉科鲁尼亚   lklny   
314370000   拉里奥哈    llah    
314380000   拉斯帕尔马斯  lspems  
314390000   莱昂  la  
314400000   莱里达 lld 
314410000   卢戈  lg  
314420000   马德里 mdl 
314430000   马拉加 mlj 
314440000   穆尔西亚    mexy    
314450000   纳瓦拉 nwl 
314460000   帕伦西亚    plxy    
314470000   蓬特韦德拉   ptwdl   
314480000   萨拉戈萨    slgs    
314490000   萨拉曼卡    slmk    
314500000   萨莫拉 sml 
314510000   塞哥维亚    sgwy    
314520000   塞维利亚    swly    
314530000   桑坦德 std 
314540000   圣克鲁斯-德特内里费  skls-dtnlf  
314550000   索里亚 sly 
314560000   塔拉戈纳    tlgn    
314570000   特鲁埃尔    tlae    
314580000   托莱多 tld 
314590000   韦尔瓦 wew 
314600000   韦斯卡 wsk 
315000000   希腊  xl  
315110000   比雷埃夫斯   blafs   
315120000   多德卡尼斯   ddkns   
315130000   干尼亚 gny 
315140000   基克拉迪    jkld    
315150000   拉西锡 lxx 
315160000   莱斯博斯    lsbs    
315170000   雷西姆农    lxmn    
315180000   萨摩斯 sms 
315190000   雅典  yd  
315200000   伊拉克里翁   ylklw   
316000000   新加坡 xjp 
317000000   新喀里多尼亚  xkldny  
318000000   新西兰 xxl 
318110000   奥克兰 akl 
318120000   北岸  ba  
318130000   北帕默斯顿   bpmsd   
318140000   北远  by  
318150000   布莱尼姆    blnm    
318160000   达尼丁 dnd 
318170000   格雷茅斯    glms    
318180000   哈密尔顿    hmed    
318190000   黑斯廷斯    hsts    
318200000   怀塔科拉    htkl    
318210000   吉斯伯恩    jsbe    
318220000   凯帕拉 kpl 
318230000   克赖斯特彻奇  klstcq  
318240000   里士满 lsm 
318250000   马努考 mnk 
318260000   纳尔逊 nex 
318270000   内皮尔 npe 
318280000   斯特拉特福德  stltfd  
318290000   陶马鲁努伊   tmlny   
318300000   瓦卡塔尼    wktn    
318310000   旺阿雷 wal 
318320000   旺格努伊    wgny    
318330000   新普利茅斯   xplms   
318340000   因弗卡吉尔   yfkje   
319000000   匈牙利 xyl 
319110000   巴兰尼亚    blny    
319120000   巴奇-基什孔  bq-jsk  
319130000   包尔绍德-奥包乌伊-曾普伦   besd-abwy-cpl   
319140000   贝凯什 bks 
319150000   布达佩斯    bdps    
319160000   费耶尔 fye 
319170000   豪伊杜-比豪尔 hyd-bhe 
319180000   赫维什 hws 
319190000   加兹-纳杰孔-索尔诺克 jz-njk-senk 
319200000   杰尔-莫松-肖普朗   je-ms-xpl   
319210000   科马罗姆    kmlm    
319220000   诺格拉德    ngld    
319230000   佩斯  ps  
319240000   琼格拉德    qgld    
319250000   绍莫吉 smj 
319260000   索博尔奇-索特马尔-贝拉格   sbeq-stme-blg   
319270000   托尔瑙 ten 
319280000   维斯普雷姆   wsplm   
319290000   沃什  ws  
319300000   佐洛  zl  
320000000   叙利亚 xly 
320110000   阿勒颇 alp 
320120000   大马士革    dmsg    
320130000   大马士革市   dmsgs   
320140000   代尔祖尔    deze    
320150000   德拉  dl  
320160000   哈马  hm  
320170000   哈塞克 hsk 
320180000   霍姆斯 hms 
320190000   加布  jb  
320200000   卡米什利    kmsl    
320210000   库奈特拉    kntl    
320220000   拉卡  lk  
320230000   拉塔基亚    ltjy    
320240000   苏韦达 swd 
320250000   塔尔图斯    tets    
320260000   伊德利卜    ydlb    
321000000   牙买加 ymj 
321110000   波特兰 btl 
321120000   汉诺威 hnw 
321130000   金斯敦 jsd 
321140000   克拉伦登    klld    
321150000   曼彻斯特    mcst    
321160000   圣安德鲁斯   sadls   
321170000   圣安娜 san 
321180000   圣凯瑟琳    sksl    
321190000   圣玛丽 sml 
321200000   圣托马斯    stms    
321210000   圣伊丽莎白   sylsb   
321220000   圣詹姆斯    szms    
321230000   特里洛尼    tlln    
321240000   西摩兰 xml 
322000000   亚美尼亚    ymny    
322110000   阿尔马维尔   aemwe   
322120000   阿拉加措特恩  aljcte  
322130000   阿拉拉特    allt    
322140000   埃里温市    alws    
322150000   格加尔库尼克  gjeknk  
322160000   科泰克 ktk 
322170000   洛里  ll  
322180000   塔武什 tws 
322190000   瓦约茨·佐尔  wyc·ze  
322200000   希拉克 xlk 
322210000   休尼克 xnk 
323000000   也门  ym  
323110000   阿比扬 aby 
323120000   阿姆兰 aml 
323130000   贝达  bd  
323140000   达利  dl  
323150000   哈德拉毛    hdlm    
323160000   哈杰  hj  
323170000   荷台达 htd 
323180000   焦夫  jf  
323190000   拉赫季 lhj 
323200000   马里卜 mlb 
323210000   迈赫拉 mhl 
323220000   迈赫维特    mhwt    
323230000   萨达  sd  
323240000   萨那  sn  
323250000   赛文  sw  
323260000   舍卜沃 sbw 
323270000   塔伊兹 tyz 
323280000   希赫尔 xhe 
323290000   亚丁  yd  
323300000   伊卜  yb  
323310000   扎玛尔 zme 
324000000   伊拉克 ylk 
325000000   伊朗  yl  
326000000   以色列 ysl 
326110000   阿什杜德    asdd    
326120000   贝尔谢巴    bexb    
326130000   贝特雁 bty 
326140000   海法  hf  
326150000   霍隆  hl  
326160000   内坦亚 nty 
326170000   特拉维夫    tlwf    
326180000   耶路撒冷    ylsl    
327000000   意大利 ydl 
327110000   阿斯蒂 asd 
327120000   阿斯科利皮切诺 asklpqn 
327130000   安科纳 akn 
327140000   奥尔比亚    aeby    
327150000   奥里斯塔诺   alstn   
327160000   奥斯塔 ast 
327170000   巴勒莫 blm 
327180000   巴里  bl  
327190000   贝加莫 bjm 
327200000   贝内文托    bnwt    
327210000   比萨  bs  
327220000   波代诺内    bdnn    
327230000   波坦察 btc 
327240000   博洛尼亚    blny    
327250000   布拉  bl  
327260000   布雷西亚    blxy    
327270000   布林迪西    bldx    
327280000   的里雅斯特   dlyst   
327290000   都灵  dl  
327300000   费拉拉 fll 
327310000   佛罗伦萨    flls    
327320000   福贾  fj  
327330000   卡利亚里    klyl    
327340000   卡塞塔 kst 
327350000   卡塔尼亚    ktny    
327360000   卡坦扎罗    ktzl    
327370000   坎波巴索    kbbs    
327380000   科摩  km  
327390000   科森扎 ksz 
327400000   克罗托内    kltn    
327410000   库内奥 kna 
327420000   拉奎拉 lkl 
327430000   拉斯佩齐亚   lspqy   
327440000   莱科  lk  
327450000   莱切  lq  
327460000   雷焦艾米利亚  ljamly  
327470000   雷焦卡拉布里亚 ljklbly 
327480000   里窝那 lwn 
327490000   罗马  lm  
327500000   马萨  ms  
327510000   马泰拉 mtl 
327520000   蒙扎  mz  
327530000   米兰  ml  
327540000   摩德纳 mdn 
327550000   墨西拿 mxn 
327560000   那不勒斯    nbls    
327570000   努奥罗 nal 
327580000   诺瓦拉 nwl 
327590000   帕尔马 pem 
327600000   帕维亚 pwy 
327610000   佩鲁贾 plj 
327620000   热那亚 rny 
327630000   萨莱诺 sln 
327640000   萨萨里 ssl 
327650000   萨沃纳 swn 
327660000   塔兰托 tlt 
327670000   特拉帕尼    tlpn    
327680000   特伦托 tlt 
327690000   威尼斯 wns 
327700000   韦尔切利    weql    
327710000   维泰博 wtb 
327720000   乌迪内 wdn 
327730000   锡拉库扎    xlkz    
327740000   锡耶纳 xyn 
327750000   亚历山德里亚  ylsdly  
327760000   伊塞尔尼亚   yseny   
328000000   印度  yd  
328110000   艾藻尔 aze 
328120000   班加罗尔    bjle    
328130000   本地治里    bdzl    
328140000   博帕尔 bpe 
328150000   布巴内斯瓦尔  bbnswe  
328160000   昌迪加尔    cdje    
328170000   达曼  dm  
328180000   第乌  dw  
328190000   甘托克 gtk 
328200000   哥印拜陀    gybt    
328210000   加尔各答    jegd    
328220000   加里加尔    jlje    
328230000   贾巴尔普尔   jbepe   
328240000   贾朗达尔    jlde    
328250000   焦特布尔    jtbe    
328260000   金奈  jn  
328270000   卡瓦拉蒂    kwld    
328280000   科希马 kxm 
328290000   马埃  ma  
328300000   马杜赖 mdl 
328310000   森伯尔布尔   sbebe   
328320000   特里凡得琅   tlfdl   
328330000   乌代布尔    wdbe    
328340000   西隆  xl  
328350000   锡尔萨瓦    xesw    
328360000   新德里 xdl 
328370000   亚南  yn  
328380000   因帕尔 ype 
328390000   印多尔 yde 
328400000   斋普尔 zpe 
329000000   印度尼西亚   ydnxy   
329110000   巴厘  bl  
329120000   邦加－勿里洞群岛    bj－wldqd    
329130000   北苏拉威西   bslwx   
329140000   北苏门答腊   bsmdl   
329150000   大雅加达首都特区    dyjdsdtq    
329160000   东加里曼丹   djlmd   
329170000   东南苏拉威西  dnslwx  
329180000   东努沙登加拉  dnsdjl  
329190000   东爪哇 dzw 
329200000   廖内  ln  
329210000   马鲁古 mlg 
329220000   明古鲁 mgl 
329230000   楠榜  nb  
329240000   南加里曼丹   njlmd   
329250000   南苏拉威西   nslwx   
329260000   南苏门答腊   nsmdl   
329270000   日惹特区    rrtq    
329280000   万丹  wd  
329290000   西努沙登加拉  xnsdjl  
329300000   西苏门答腊   xsmdl   
329310000   西爪哇 xzw 
329320000   雅加达 yjd 
329330000   亚齐  yq  
329340000   伊里安查亚   ylacy   
329350000   占碑  zb  
329360000   中加里曼丹   zjlmd   
329370000   中苏拉威西   zslwx   
329380000   中爪哇 zzw 
330000000   英国  yg  
330110000   北爱尔兰    bael    
330110100   贝尔法斯特   befst   
330110200   德里  dl  
330110300   利斯本 lsb 
330110400   纽里  nl  
330120000   苏格兰 sgl 
330120100   阿伯丁 abd 
330120200   爱丁堡 adb 
330120300   丹迪  dd  
330120400   格拉斯哥    glsg    
330120500   斯特灵 stl 
330120600   因弗内斯    yfns    
330130000   威尔士 wes 
330130100   班戈  bg  
330130200   卡迪夫 kdf 
330130300   纽波特 nbt 
330130400   斯旺西 swx 
330140000   英格兰 ygl 
330140100   埃克塞特    akst    
330140200   巴斯  bs  
330140300   彼得伯勒    bdbl    
330140400   伯明翰 bmh 
330140500   布拉德福德   bldfd   
330140600   布莱顿与赫福  bldyhf  
330140700   布里斯托尔   blste   
330140800   德比  db  
330140900   德罕  dh  
330141000   格洛斯特    glst    
330141100   赫尔河畔京斯敦 hehpjsd 
330141200   赫里福德    hlfd    
330141300   剑桥  jq  
330141400   卡莱尔 kle 
330141500   坎特伯雷    ktbl    
330141600   考文垂 kwc 
330141700   兰开斯特    lkst    
330141800   里彭  lp  
330141900   利奇菲尔德   lqfed   
330142000   利物浦 lwp 
330142100   利茲  lz  
330142200   列斯特 lst 
330142300   林肯  lk  
330142400   伦敦  ld  
330142500   曼彻斯特    mcst    
330142600   南安普敦    napd    
330142700   牛津  nj  
330142800   纽卡斯尔    nkse    
330142900   诺丁汉 ndh 
330143000   诺里奇 nlq 
330143100   朴茨茅斯    pcms    
330143200   普雷斯顿    plsd    
330143300   普利茅斯    plms    
330143400   奇切斯特    qqst    
330143500   切斯特 qst 
330143600   桑德兰 sdl 
330143700   圣阿本斯    sabs    
330143800   索尔斯堡    sesb    
330143900   索福特 sft 
330144000   特鲁罗 tll 
330144100   特伦特河畔斯多克    tlthpsdk    
330144200   威尔斯 wes 
330144300   韦克菲尔德   wkfed   
330144400   温彻斯特    wcst    
330144500   伍尔弗汉普顿  wefhpd  
330144600   伍斯特 wst 
330144700   谢菲尔德    xfed    
330144800   伊利  yl  
330144900   约克  yk  
331000000   英属印度洋领地 ysydyld 
332000000   约旦  yd  
332110000   阿吉隆 ajl 
332120000   安曼  am  
332130000   拜勒加 blj 
332140000   杰拉什 jls 
332150000   卡拉克 klk 
332160000   鲁赛法 lsf 
332170000   马安  ma  
332180000   马德巴 mdb 
332190000   马夫拉克    mflk    
332200000   塔菲拉 tfl 
332210000   亚喀巴 ykb 
332220000   伊尔比德    yebd    
332230000   扎尔卡 zek 
333000000   越南  yn  
333110000   海防  hf  
333120000   河内  hn  
333130000   胡志明市    hzms    
334000000   赞比亚 zby 
334110000   北方  bf  
334120000   东方  df  
334130000   卢阿普拉    lapl    
334140000   卢萨卡 lsk 
334150000   南方  nf  
334160000   铜带  td  
334170000   西北  xb  
334180000   西方  xf  
334190000   中央  zy  
335000000   泽西岛 zxd 
336000000   乍得  zd  
337000000   直布罗陀    zblt    
338000000   智利  zl  
338110000   阿劳卡尼亚大区 alknydq 
338120000   阿塔卡马大区  atkmdq  
338130000   安托法加斯塔大区    atfjstdq    
338140000   比奥比奥大区  babadq  
338150000   复活节岛    fhjd    
338160000   湖大区 hdq 
338170000   科金博大区   kjbdq   
338180000   马乌莱大区   mwldq   
338190000   麦哲伦-智利南极大区  mzl-zlnjdq  
338200000   圣地亚哥    sdyg    
338210000   塔拉帕卡大区  tlpkdq  
338220000   瓦尔帕莱索大区 weplsdq 
338230000   伊瓦涅斯将军的艾森大区 ywnsjjdasdq 
339000000   中非共和国   zfghg   
339110000   巴明吉-班戈兰 bmj-bgl 
339120000   班吉直辖市   bjzxs   
339130000   宾博  bb  
339140000   凯莫  km  
339150000   洛巴伊 lby 
339160000   曼贝雷-卡代  mbl-kd  
339170000   姆博穆 mbm 
339180000   纳纳-格里比齐 nn-glbq 
339190000   纳纳-曼贝雷  nn-mbl  
339200000   桑加-姆巴埃雷 sj-mbal 
339210000   上科托 skt 
339220000   上姆博穆    smbm    
339230000   瓦卡  wk  
339240000   瓦卡加 wkj 
339250000   瓦姆  wm  
339260000   瓦姆-彭代   wm-pd   
339270000   翁贝拉-姆波科 wbl-mbk 
339280000   下科托 xkt 
"""

datas = datas.replace("\n", " ").split(" ")

formet_data = []
element = []
for data in datas:
    if data in ['"'] or not data:
        continue
    if data.isdigit():
        element = []
        element.append(data)
    else:
        element.append(data)
    if element not in formet_data:
        formet_data.append(element)

# formet_data = [ele.append("") and tuple(ele) if len(ele)==3 else tuple(ele) for ele in formet_data ]
formet_data_new = []
for ele in formet_data:
    if len(ele) == 3:
        ele.append("")
    formet_data_new.append(tuple(ele))
# print(formet_data_new)

inset_sql = "insert into regions(id,name,first_spell,full_spell) values(%s,%s,%s,%s)"
mysql.insertMany(inset_sql, formet_data_new)
mysql.dispose()
print(formet_data)
