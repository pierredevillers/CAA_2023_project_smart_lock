{"components":[{"id":"_coretwoscreen","createTime":1684133765613,"name":"screen","x":0,"y":0,"width":320,"height":240,"backgroundColor":"#FFFFFF","backgroundImage":"","size":0,"screenType":"default","type":"screen"},{"id":"____buttonA","createTime":1684133765613,"name":"ButtonA","buttonIndex":0,"x":35,"y":216,"width":64,"height":24,"text":"ButtonA","visibility":false,"type":"button"},{"id":"____buttonB","createTime":1684133765613,"name":"ButtonB","buttonIndex":1,"x":125,"y":216,"width":64,"height":24,"text":"ButtonB","visibility":false,"type":"button"},{"id":"____buttonC","createTime":1684133765614,"name":"ButtonC","buttonIndex":2,"x":215,"y":216,"width":64,"height":24,"text":"ButtonC","visibility":false,"type":"button"},{"id":"+5o4k&Kw4=Rugw*m","createTime":1684134585792,"isCoreTwo":true,"isPaper":false,"name":"label0","x":238,"y":77,"color":"#000","text":"label0","font":"FONT_MONT_14","rotation":0,"screenType":"default","type":"label","layer":5,"width":null,"height":null,"radius":null},{"id":"Sn*vR7GRMqdFwFan","createTime":1684134645827,"isCoreTwo":true,"isPaper":false,"name":"label1","x":243,"y":102,"color":"#000","text":"label1","font":"FONT_MONT_14","rotation":0,"screenType":"default","type":"label","layer":7,"width":null,"height":null,"radius":null},{"id":"P`S6uw0m8LI%rJZH","createTime":1684134648173,"isCoreTwo":true,"isPaper":false,"name":"label2","x":248,"y":129,"color":"#000","text":"label2","font":"FONT_MONT_14","rotation":0,"screenType":"default","type":"label","layer":9,"width":null,"height":null,"radius":null},{"id":"-_iiRHhwy$HPqzUO","createTime":1684134990035,"isCoreTwo":true,"isPaper":false,"name":"label3","x":238,"y":154,"color":"#000","text":"label3","font":"FONT_MONT_14","rotation":0,"screenType":"default","type":"label","layer":11,"width":null,"height":null,"radius":null}],"type":"core2","versions":"Beta","units":[{"id":"q=_C@q!rV8gxBC*=","createTime":1684133845975,"type":"gps","name":"gps_0","port":"C","default":["A","B","C","E","Custom"],"user_port":["21","22"],"icon":"unit_gps.png","hasPnP":true,"url":"https://docs.m5stack.com/en/unit/gps","new_port":"C","new_default":["A","B","C","E","Custom"]}],"hats":[],"stamps":[],"blockly":"<block type=\"basic_on_setup\" id=\"setup_block\" deletable=\"false\" x=\"50\" y=\"50\"><next><block type=\"basic_on_loop\" id=\"ZlqX)W$IRdj)G)!EMwPT\"><statement name=\"LOOP\"><block type=\"label_set_text\" id=\"LAAmtP-9*mRbO_htPekm\"><field name=\"COMPONENT\">label0</field><value name=\"TEXT\"><shadow type=\"text\" id=\"jP.=a}QlF/LgU^!F*D|G\"><field name=\"TEXT\">Hello M5</field></shadow><block type=\"unit_gps_get_latitude_decimal\" id=\"Ao$_1JpLDZ2e-B]R?A*=\"><field name=\"latitude\">gps_0</field></block></value><next><block type=\"label_set_text\" id=\"9K#h-{X5fhj4[#hBGx4l\"><field name=\"COMPONENT\">label1</field><value name=\"TEXT\"><shadow type=\"text\" id=\"([Zp/?G7N=2vij@`F6=/\"><field name=\"TEXT\">Hello M5</field></shadow><block type=\"unit_gps_get_state\" id=\"L?885M[IwOK7bm4SfM%E\"><field name=\"gps\">gps_0</field></block></value><next><block type=\"label_set_text\" id=\"EXI5T!VPTp*88|GQ4ao[\"><field name=\"COMPONENT\">label2</field><value name=\"TEXT\"><shadow type=\"text\"><field name=\"TEXT\">Hello M5</field></shadow><block type=\"unit_gps_get_longitude_decimal\" id=\"I]6T3GWki6+ZRGu|ITwC\"><field name=\"longitude\">gps_0</field></block></value><next><block type=\"label_set_text\" id=\")9HRCo.K=%vPBDGn42HL\"><field name=\"COMPONENT\">label3</field><value name=\"TEXT\"><shadow type=\"text\"><field name=\"TEXT\">Hello M5</field></shadow><block type=\"unit_gps_get_positioning_quality\" id=\"1H^4L[`@Igx`NGPy.vUi\"><field name=\"positioning\">gps_0</field></block></value></block></next></block></next></block></next></block></statement></block></next></block>","Blockly.Remotes":[],"Blockly.RemotePlus":[{"id":"__title","blockId":"","createTime":1684133765604,"name":"M5RemoteTitle","dragAndDrop":false,"resizable":false,"options":{"minWidth":1,"minHeight":1,"maxWidth":6,"maxHeight":10,"defaultWidth":2,"defaultHeight":1},"w":2,"h":1,"bgColor":"#0080FF","color":"#fff","fontsize":"M","label":"M5Remote","interval":3000,"code":"","event":"","dataSource":"none","ezdataToken":"Q6xlmHu1Rb1MES12c50PRsPjYXVTZ21L","topic":"","needShadow":false,"type":"title","x":null,"y":null}],"modules":[],"cbIdList_":[],"eventCBIdList_":[],"apikey":"7AA57340","uuid":"688ae9a5-7421-4da4-9dae-40b7283ea289"}