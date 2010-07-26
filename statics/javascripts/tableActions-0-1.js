/*
        Table actions plug-in v0.1 by frequency-decoder.com

        Released under a creative commons Attribution-ShareAlike 2.5 license (http://creativecommons.org/licenses/by-sa/2.5/)

        Please credit frequency decoder in any derivative work - thanks

        You are free:

        * to copy, distribute, display, and perform the work
        * to make derivative works
        * to make commercial use of the work

        Under the following conditions:

                by Attribution.
                --------------
                You must attribute the work in the manner specified by the author or licensor.

                sa
                --
                Share Alike. If you alter, transform, or build upon this work, you may distribute the resulting work only under a license identical to this one.

        * For any reuse or distribution, you must make clear to others the license terms of this work.
        * Any of these conditions can be waived if you get permission from the copyright holder.
        
        NOTE: This work is based on a script originally developped by the veritable Richard Cornford (http://www.litotes.demon.co.uk/example_scripts/tableHighlighter.html)
*/
var fdTableActions = {
        tableCache:{},
        /*@cc_on
        /*@if (@_jscript_version <= 5.6)
        ieEventCache:[],
        /*@end
        @*/
        init:function() {
                var tables = document.getElementsByTagName("table");
                var rowStyleAlt, highlightCol, start, trs, rowSelect, rowSelectCallback;
                var uniqueID = 0;
                var colspan = "colspan";
                var rowspan = "rowspan";
                
                // Internet Explorer seems to require a camelCased colSpan & rowSpan
                /*@cc_on
                /*@if(@_win32)
                colspan = "colSpan";
                rowspan = "rowSpan";
                /*@end
                @*/
                
                // Loop through all the tables
                var celCount, rowL, colL, rowLength, workArr, rowSpan, colSpan, cel, colObj, elem, rowList, rowArr, fnc, colHead;

                for(var k = 0, table; table = tables[k]; k++) {
                        // Grab the className for the alternate rows
                        rowAlt  = table.className.search(/rowstyle-([\S-]+)/) == -1 ? "" : table.className.match(/rowstyle-([\S]+)/)[1];
                        // Highlight columns?
                        highlightCol  = table.className.search(/highlight-column/) != -1;
                        // Grab the className for the rowStyleHover
                        rowHover  = table.className.search(/rowstylehover-([\S-]+)/) == -1 ? "" : table.className.match(/rowstylehover-([\S]+)/)[1];
                        // Do we select the rows
                        rowSelect = table.className.search(/rowselect-([\S-]+)/) == -1 ? "" : table.className.match(/rowselect-([\S]+)/)[1];
                        // Do we have a callback for this table whenever a row is selected?
                        rowSelectCallback = table.className.search(/rowselectcallback-([\S-]+)/) == -1 ? "" : table.className.match(/rowselectcallback-([\S]+)/)[1];
                        // Current TH or TD
                        cellHover = table.className.search(/cellhover-([\S-]+)/) == -1 ? "" : table.className.match(/cellhover-([\S]+)/)[1];
                        // Replace "-" with "." to enable Object.method callbacks
                        rowSelectCallback = rowSelectCallback.replace("-", ".");
                        
                        // Do we even need to continue?
                        if(!rowAlt && !rowHover && !rowSelect) continue;
                        
                        // Create a table ID if necessary
                        if(!table.id) table.id = "fdTable-" + uniqueID++;
                        
                        // Cache this tables details
                        fdTableActions.tableCache[table.id] = { "trCache":[], "rowSelect":rowSelect };

                        // Grab the table's TR nodes
                        rowArr = [];
                        rowList = table.getElementsByTagName('tr');

                        for(var i = 0;i < rowList.length;i++){
                                colObj = [];
                                elem = rowList[i].firstChild;
                                do {
                                        if(elem.tagName && elem.tagName.toLowerCase().search(/td|th/) != -1) {
                                                colObj[colObj.length] = elem;
                                        };
                                        elem = elem.nextSibling;
                                } while(elem);
                                // Stripe the row if needs be
                                if(i % 2 == 0 && rowAlt) rowList[i].className += " " + rowAlt;
                                rowArr[rowArr.length] = colObj;
                        };

                        // Don't continue if we only need to zebra stripe the table rows
                        if(!rowHover && !rowSelect) continue;

                        if(rowArr.length > 0){
                                /* Attribution: Parts of the following code based on an original script by Richard Cornford (http://www.litotes.demon.co.uk/example_scripts/tableHighlighter.html) */
                                rowLength = rowArr[0].length;
                                for(var c = 0;c < rowArr[0].length;c++){
                                        if(rowArr[0][c].getAttribute(colspan) > 1){
                                                rowLength = rowLength + (rowArr[0][c].getAttribute(colspan) - 1);
                                        };
                                };

                                workArr  = new Array(rowArr.length);
                                for(var c = rowArr.length;c--;){
                                        workArr[c]  = new Array(rowLength);
                                };

                                for(var c = 0;c < workArr.length;c++) {
                                        celCount = 0;
                                        for(var i = 0;i < rowLength;i++) {
                                                if(!workArr[c][i]) {
                                                        cel = rowArr[c][celCount];
                                                        colSpan = (cel.getAttribute(colspan) && cel.getAttribute(colspan) > 1) ? cel.getAttribute(colspan) : 1;
                                                        rowSpan = (cel.getAttribute(rowspan) && cel.getAttribute(rowspan) > 1) ? cel.getAttribute(rowspan) : 1;

                                                        for(var t = 0;((t < colSpan)&&((i+t) < rowLength));t++){
                                                                for(var n = 0;((n < rowSpan)&&((c+n) < workArr.length));n++){
                                                                        workArr[(c+n)][(i+t)] = cel;
                                                                };
                                                        };
                                                        if(++celCount == rowArr[c].length) break;
                                                };
                                        };
                                };
                                /* End attribution */
                                
                                rowArr = [];
                                colHead = new Array(rowLength);
                                for(var c = workArr.length;c--;) {
                                        for(var i = rowLength;i--;) {
                                                if(!colHead[i]) colHead[i] = [];
                                                if(workArr[c][i]) {
                                                        var notFound = true;
                                                        for(var t = 0, cell; cell = colHead[i][t];t++) {
                                                                if(cell == workArr[c][i]) {
                                                                        notFound = false;
                                                                        break;
                                                                };
                                                        };
                                                        if(notFound) {
                                                                colHead[i][colHead[i].length] = workArr[c][i];
                                                        };
                                                };
                                        };
                                };

                                fdTableActions.tableCache[table.id].colCache = colHead;

                                rowL = workArr.length;
                                for(var c = 0; c < rowL; c++) {
                                        colL = workArr[c].length;
                                        for(var i = 0; i < colL;i++) {
                                                if(workArr[c][i] && workArr[c][i].className.search("fdCellProcessed") == -1) {
                                                        colSpan = (workArr[c][i].getAttribute(colspan) && workArr[c][i].getAttribute(colspan) > 1) ? workArr[c][i].getAttribute(colspan) : 1;

                                                        if(rowHover) {
                                                                fnc = '';

                                                                if(highlightCol) {
                                                                        fnc =   'for(col = '+i+'; col < '+(i + Number(colSpan))+'; col++) {elemArr =  fdTableActions.tableCache["'+table.id+'"].colCache[col];for(var ec = 0, elem; elem = elemArr[ec]; ec++) {if(e.type == "mouseover") {if(elem.className.search("'+rowHover+'") == -1) { elem.className += " '+rowHover+'"; };} else {elem.className = elem.className.replace("'+rowHover+'", "");};};};';
                                                                };

                                                                /*@cc_on
                                                                var tmp = 'var tr = this.parentNode; if(e.type == "mouseover") { tr.className += " '+rowHover+'"; } else { tr.className = tr.className.replace("'+rowHover+'", "");};';
                                                                @if (@_jscript_version >= 5.7)
                                                                        if(document.compatMode == "BackCompat") fnc += tmp;
                                                                @else
                                                                        fnc += tmp;
                                                                @end
                                                                @*/

                                                                if(cellHover) {
                                                                        fnc += 'if(e.type == "mouseover") { this.className += " '+cellHover+'"; } else { this.className = this.className.replace("'+cellHover+'", ""); };';
                                                                };

                                                                if(fnc) {
                                                                        fnc = 'var eventWrapper = function eventWrapper(e) { e = e || window.event; ' + fnc + '};'
                                                                        eval(fnc);
                                                                        fdTableActions.addEvent(workArr[c][i], "mouseover", eventWrapper);
                                                                        fdTableActions.addEvent(workArr[c][i], "mouseout",  eventWrapper);
                                                                        eventWrapper = null;
                                                                };
                                                        };

                                                        if(rowSelect) {
                                                                fnc = 'var eventWrapper = function eventWrapper(e) { e = e || window.event; var tr = this.parentNode; if(tr.nodeType == 3) { tr = tr.parentNode; }; if(tr.className.search("'+rowSelect+'") != -1) { tr.className = tr.className.replace("'+rowSelect+'", ""); var rowArr = []; for(var i = 0, elem; elem = fdTableActions.tableCache["'+table.id+'"].trCache[i]; i++) { if(elem != tr) rowArr[rowArr.length] = elem; }; fdTableActions.tableCache["'+table.id+'"].trCache = rowArr; } else { tr.className += " '+rowSelect+'"; fdTableActions.tableCache["'+table.id+'"].trCache[fdTableActions.tableCache["'+table.id+'"].trCache.length] = tr; }; ';

                                                                // Object callback
                                                                if(rowSelectCallback.search(".") != -1) {
                                                                        fnc = fnc + 'var split = "'+rowSelectCallback+'".split("."); var func = window; for(var i = 0, f; f = split[i]; i++) { if(f in func) { func = func[f]; } else { break; }; }; if(typeof func == "function") { func(fdTableActions.tableCache["'+table.id+'"].trCache.concat([])); return; };';
                                                                };

                                                                // Function callback
                                                                if(rowSelectCallback) {
                                                                        fnc = fnc + 'if("'+rowSelectCallback+'" in window) { window[fdTableActions.tableCache["'+table.id+'"].rowSelectCallback](fdTableActions.tableCache["'+table.id+'"].trCache.concat([]));} else ';
                                                                };

                                                                // Default callback 'rowSelectCallback'
                                                                fnc = fnc + 'if("rowSelectCallback" in window) { window["rowSelectCallback"]("'+table.id+'", fdTableActions.tableCache["'+table.id+'"].trCache.concat([])); }; };';
                                                                eval(fnc);
                                                                fdTableActions.addEvent(workArr[c][i], "click", eventWrapper);
                                                                eventWrapper = null;
                                                        };
                                                        
                                                        workArr[c][i].className += " fdCellProcessed";
                                                };
                                        };
                                };
                        };
                };
        },
        deselectAllRows:function(tableId) {
                if(!(tableId in fdTableActions.tableCache) || !fdTableActions.tableCache[tableId].rowSelect) return;
                var trList = fdTableActions.tableCache[tableId].trCache;
                for(var i = trList.length; i--;) {
                        trList[i].className = trList[i].className.replace(fdTableActions.tableCache[tableId].rowSelect, "");
                };
                fdTableActions.tableCache[tableId].trCache = [];
                trList = null;
        },
        unLoad:function() {
                /*@cc_on
                /*@if (@_jscript_version <= 5.6)
                var obj, type, fn;
                for(var i = 0; i < fdTableActions.ieEventCache.length; i++) {
                        obj  = fdTableActions.ieEventCache[i][0];
                        type = fdTableActions.ieEventCache[i][1];
                        fn   = fdTableActions.ieEventCache[i][2];
                        obj.detachEvent( "on"+type, obj[type+fn] );
                        obj["e"+type+fn] = obj[type+fn] = null;
                };
                fdTableActions.ieEventCache = null;
                fdTableActions.tableCache = null;
                /*@end
                @*/
        },
        addEvent:function(obj, type, fn) {
                if( obj.attachEvent ) {
                        /*@cc_on
                        /*@if (@_jscript_version <= 5.6)
                        fdTableActions.ieEventCache[fdTableActions.ieEventCache.length] = [obj, type, fn],
                        /*@end
                        @*/
                        obj["e"+type+fn] = fn;
                        obj[type+fn] = function(){obj["e"+type+fn]( window.event );};
                        obj.attachEvent( "on"+type, obj[type+fn] );
                } else {obj.addEventListener( type, fn, true );};
        }
};

fdTableActions.addEvent(window, "load", fdTableActions.init);
/*@cc_on
/*@if (@_jscript_version <= 5.6)
fdTableActions.addEvent(window, "unload", fdTableActions.unLoad);
/*@end
@*/
