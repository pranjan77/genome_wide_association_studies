# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import subprocess
import uuid
from KBaseReport.KBaseReportClient import KBaseReport
from DataFileUtil.DataFileUtilClient import DataFileUtil
from genome_wide_association_studies.Utils import gwas_results_utils 



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
    GIT_COMMIT_HASH = "fb9bc0c5d00a0314e9f832d30a996c7448e61db9"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.scratch = os.path.abspath(config['scratch'])
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
       # self.shared_folder = os.path.abspath(config['scratch'])
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

        #Download file from staging area
        params = import_gwas_data_params
        print (params)
#        print (import_gwas_data_params)

#        download_staging_file_params = {
#            'staging_file_subdir_path': params.get('staging_file_subdir_path')
#       }
#        try:
#            scratch_file_path = self.dfu.download_staging_file(
#                      download_staging_file_params).get('copy_file_path')
#        except:
#            raise ValueError ('error uploading HTML file to shock')
        gwas_utils = gwas_results_utils.gwas_results_utils(self.config)



        returnVal = gwas_utils.run_import_gwas_results(params)

        #END import_gwas_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_gwas_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def import_snp_data(self, ctx, import_snp_data_params):
        """
        :param import_snp_data_params: instance of type
           "import_snp_data_params" -> structure: parameter "input_shock_id"
           of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_snp_data_result" -> structure:
           parameter "report_ref" of String, parameter "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_snp_data
        params = import_snp_data_params
        print (import_snp_data_params)

        download_staging_file_params = {
            'staging_file_subdir_path': params.get('staging_file_subdir_path')
        }
        try:
            scratch_file_path = self.dfu.download_staging_file(
                      download_staging_file_params).get('copy_file_path')
        except:
            raise ValueError ('error uploading HTML file to shock')

        #END import_snp_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_snp_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def import_trait_data(self, ctx, import_trait_data_params):
        """
        :param import_trait_data_params: instance of type
           "import_trait_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_trait_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_trait_data
        params = import_trait_data_params
        print (import_trait_data_params)

        download_staging_file_params = {
            'staging_file_subdir_path': params.get('staging_file_subdir_path')
        }
        try:
            scratch_file_path = self.dfu.download_staging_file(
                      download_staging_file_params).get('copy_file_path')
        except:
            raise ValueError ('error uploading HTML file to shock')
        #END import_trait_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_trait_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def import_network_data(self, ctx, import_network_data_params):
        """
        :param import_network_data_params: instance of type
           "import_network_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_network_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_network_data
        params = import_network_data_params
        print (import_network_data_params)

        download_staging_file_params = {
            'staging_file_subdir_path': params.get('staging_file_subdir_path')
        }
        try:
            scratch_file_path = self.dfu.download_staging_file(
                      download_staging_file_params).get('copy_file_path')
        except:
            raise ValueError ('error uploading HTML file to shock')
        #END import_network_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_network_data return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def import_motif_data(self, ctx, import_motif_data_params):
        """
        :param import_motif_data_params: instance of type
           "import_motif_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_motif_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_motif_data
        #END import_motif_data

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_motif_data return value ' +
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
