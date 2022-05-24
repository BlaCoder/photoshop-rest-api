from photoshop import api as ps
from setup.settings import MEDIA_ROOT

class Activate():
    def exec(codigo, usuario, ambiente, itens):
        
        photoshop = ps.Application()
        
        jsx = r"""
        var startRulerUnits = app.preferences.rulerUnits
        var startDisplayDialogs = app.displayDialogs

        app.preferences.rulerUnits = Units.CM
        app.preferences.displayDialogs = DialogModes.NO

        var codigo = '""" + codigo + """';
        var usuario = '""" + usuario + """';
        var ambiente = '""" + ambiente + """';
        var itens_naoTratado = '""" + itens + """';
        var itens = itens_naoTratado.split(',')

        var sfwOptions = new ExportOptionsSaveForWeb();   
        sfwOptions.format = SaveDocumentType.JPEG;   
        sfwOptions.includeProfile = false;   
        sfwOptions.interlaced = false;   
        sfwOptions.optimized = true;   
        sfwOptions.quality = 83;

        // alert(documento.path)

        var salvamento = new File( "C:/Users/costt/Armazenamento/dev/_definitive/media_root/" + codigo + "_" + usuario + "_" + ambiente + ".jpg" )

        function SubstituiEstampa(estampa) {
            var idplacedLayerReplaceContents = stringIDToTypeID( "placedLayerReplaceContents" );
            var desc1852 = new ActionDescriptor();
            var idnull = charIDToTypeID( "null" );
            desc1852.putPath( idnull, new File( "E:/_Unificado_Python/" + estampa + ".jpg" ) );
            executeAction( idplacedLayerReplaceContents, desc1852, DialogModes.NO );
        }

        function Abre(caminho) {
            var idOpn = charIDToTypeID( "Opn " );
            var desc10 = new ActionDescriptor();
            var iddontRecord = stringIDToTypeID( "dontRecord" );
            desc10.putBoolean( iddontRecord, false );
            var idforceNotify = stringIDToTypeID( "forceNotify" );
            desc10.putBoolean( idforceNotify, true );
            var idnull = charIDToTypeID( "null" );
            desc10.putPath( idnull, new File( caminho ) );
            var idDocI = charIDToTypeID( "DocI" );
            desc10.putInteger( idDocI, 219 );
        executeAction( idOpn, desc10, DialogModes.NO );
        }


        //////////////////////////////////////////////////////////////////////////////////////////////////////////


        function SalaBoho(almofadaQuad1,papel) {
            Abre("C:/Users/costt/Armazenamento/dev/_definitive/api/assets/UAU_SalaBoho.tif")
            var documento = app.activeDocument;
            
            if (almofadaQuad1 != '---') {
                documento.artLayers[0].visible = false
                documento.activeLayer = documento.artLayers[5]
                SubstituiEstampa(almofadaQuad1)
            } else {
                documento.artLayers[0].visible = true
            }

            if (papel != '---') {
                documento.artLayers[7].visible = true
                documento.activeLayer = documento.artLayers[7]
                SubstituiEstampa(papel)
            } else {
                documento.artLayers[7].visible = false
            }

            documento.exportDocument( salvamento, ExportType.SAVEFORWEB, sfwOptions );
            documento.close(SaveOptions.DONOTSAVECHANGES);
        }

        function Sala(almofadaQuad1, almofadaQuad2, almofadaQuad3, almofadaRet1, almofadaRet2, papel) {
            Abre("C:/Users/costt/Armazenamento/dev/_definitive/api/assets/UAU_Sala.tif")
            var documento = app.activeDocument;

            if (almofadaQuad1 != '---') {
                documento.artLayers[0].visible = false
                documento.activeLayer = documento.artLayers[10]
                SubstituiEstampa(almofadaQuad1)
            } else {
                documento.artLayers[0].visible = true
            }

            if (almofadaQuad2 != '---') {
                documento.artLayers[1].visible = false
                documento.activeLayer = documento.artLayers[12]
                SubstituiEstampa(almofadaQuad2)
            } else {
                documento.artLayers[1].visible = true
            }

            if (almofadaQuad3 != '---') {
                documento.artLayers[2].visible = false
                documento.activeLayer = documento.artLayers[18]
                SubstituiEstampa(almofadaQuad3)
            } else {
                documento.artLayers[2].visible = true
            }

            if (almofadaRet1 != '---') {
                documento.artLayers[3].visible = false
                documento.activeLayer = documento.artLayers[14]
                SubstituiEstampa(almofadaRet1)
            } else {
                documento.artLayers[3].visible = true
            }

            if (almofadaRet2 != '---') {
                documento.artLayers[4].visible = false
                documento.activeLayer = documento.artLayers[16]
                SubstituiEstampa(almofadaRet2)
            } else {
                documento.artLayers[4].visible = true
            }

            if (papel != '---') {
                documento.artLayers[20].visible = true
                documento.activeLayer = documento.artLayers[20]
                SubstituiEstampa(papel)
            } else {
                documento.artLayers[20].visible = false
            }

            documento.exportDocument( salvamento, ExportType.SAVEFORWEB, sfwOptions );
            documento.close(SaveOptions.DONOTSAVECHANGES);
        } 

        function QuartoJuvenil(almofadaQuad1, almofadaRet1, papel) {
            Abre("C:/Users/costt/Armazenamento/dev/_definitive/api/assets/UAU_QuartoJuvenil.tif")
            var documento = app.activeDocument;

            if (almofadaQuad1 != '---') {
                documento.artLayers[0].visible = false
                documento.activeLayer = documento.artLayers[6]
                SubstituiEstampa(almofadaQuad1)
            } else {
                documento.artLayers[0].visible = true
            }

            if (almofadaRet1 != '---') {
                documento.artLayers[1].visible = false
                documento.activeLayer = documento.artLayers[8]
                SubstituiEstampa(almofadaRet1)
            } else {
                documento.artLayers[1].visible = true
            }

            if (papel != '---') {
                documento.artLayers[10].visible = true
                documento.activeLayer = documento.artLayers[10]
                SubstituiEstampa(papel)
            } else {
                documento.artLayers[10].visible = false
            }

            documento.exportDocument( salvamento, ExportType.SAVEFORWEB, sfwOptions );
            documento.close(SaveOptions.DONOTSAVECHANGES);
        }

        function QuartoBebe(papel) {
            Abre("C:/Users/costt/Armazenamento/dev/_definitive/api/assets/UAU_QuartoBebe.tif")
            var documento = app.activeDocument;

            if (papel != '---') {
                documento.artLayers[4].visible = true
                documento.activeLayer = documento.artLayers[4]
                SubstituiEstampa(papel)
            } else {
                documento.artLayers[4].visible = false
            }

            documento.exportDocument( salvamento, ExportType.SAVEFORWEB, sfwOptions );
            documento.close(SaveOptions.DONOTSAVECHANGES);
        }


        ///////////////////////////////////////////////////////////////////////////////////////////////////////////

        if (ambiente == 'SalaBoho') {
            SalaBoho(itens[0],itens[1]);
        }

        if (ambiente == 'Sala') {
            Sala(itens[0],itens[1],itens[2],itens[3],itens[4],itens[5]);
        }

        if (ambiente == 'QuartoJuvenil') {
            QuartoJuvenil(itens[0],itens[1],itens[2]);
        }

        if (ambiente == 'QuartoBebe') {
            QuartoBebe(itens[0]);
        }

        app.preferences.rulerUnits = startRulerUnits
        app.preferences.displayDialogs = startDisplayDialogs
        """
        try:
            photoshop.doJavascript(jsx)
            resp = 'Ambientada feita'
        except Exception as e:
            resp = 'Erro de execução:' + e
        
        return resp