# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import subprocess
import uuid
from KBaseReport.KBaseReportClient import KBaseReport
from DataFileUtil.DataFileUtilClient import DataFileUtil
#END_HEADER


class genome_wide_association_studies:
    '''
    Module Name:
    genome_wide_association_studies

    Module Description:
    A KBase module: genome_wide_association_studies
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:pranjan77/genome_wide_association_studies"
    GIT_COMMIT_HASH = "798020bee05231e43b71c2de630b3097e502aeaf"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.scratch = os.path.abspath(config['scratch'])
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.dfu = DataFileUtil(self.callbackURL)

        #END_CONSTRUCTOR
        pass


    def import_gwas_data(self, ctx, import_gwas_data_params):
        """
        :param import_gwas_data_params: instance of type
           "import_gwas_data_params" (Insert your typespec information here.)
           -> structure: parameter "input_shock_id" of String, parameter
           "input_file_path" of String
        :returns: instance of type "Run_import_gwas_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_gwas_data
        params = import_gwas_data_params
        print import_gwas_data_params
        download_staging_file_params = {
            'staging_file_subdir_path': params.get('staging_file_subdir_path')
        }
        scratch_file_path = self.dfu.download_staging_file(
                      download_staging_file_params).get('copy_file_path')

#        import_gwas_data_params = params
        import_gwas_data_params['input_file_path'] = scratch_file_path

        print import_gwas_data_params['input_file_path'] 
        # Open the file with read only permit
#        f = open('my_text_file.txt')
#        line = f.readline()
#        while line:
#            print(line)
#            line = f.readline()
#        f.close()

       # timestamp = str(timestamp)
        htmlDir = self.shared_folder + '/html' + "123"
        os.mkdir(htmlDir)

        indexhtmlstr = '<html><body> '  + "fileStr" + ' </body></html>'
        with open(htmlDir + '/index.html','w') as indexhtml:
            indexhtml.write(indexhtmlstr)

       

        try:
            html_upload_ret = self.dfu.file_to_shock({'file_path': htmlDir ,'make_handle': 0, 'pack': 'zip'})
        except:
            raise ValueError ('error uploading HTML file to shock')

        reportName = 'import_gwas_data_'+str(uuid.uuid4())

        reportObj = {'objects_created': [],
                     'message': '',
                     'direct_html': None,
                     'direct_html_index': 0,
                     'file_links': [],
                     'html_links': [],
                     'html_window_height': 220,
                     'workspace_name': params['workspace_name'],
                     'report_object_name': reportName
                     }


        reportObj['direct_html'] = ''
        reportObj['direct_html_link_index'] = 0
        reportObj['html_links'] = [{'shock_id': html_upload_ret['shock_id'],
                                    'name': 'index.html',
                                    'label': 'Save promoter_download.zip'
                                    }]
        report = KBaseReport(self.callbackURL, token=ctx['token'])
        #report_info = report.create({'report':reportObj, 'workspace_name':input_params['input_ws']})
        report_info = report.create_extended_report(reportObj)
        returnVal = { 'report_name': report_info['name'], 'report_ref': report_info['ref'] }


        #END import_gwas_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_gwas_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
