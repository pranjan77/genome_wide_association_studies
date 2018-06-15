# -*- coding: utf-8 -*-
#BEGIN_HEADER
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
        print import_gwas_data_params
#        download_staging_file_params = {
#            'staging_file_subdir_path': params.get('staging_file_subdir_path')
#        }
#        scratch_file_path = self.dfu.download_staging_file(
#                       download_staging_file_params).get('copy_file_path')

#        import_gwas_data_params = params
#        import_gwas_data_params['input_file_path'] = scratch_file_path
        # Open the file with read only permit
#        f = open('my_text_file.txt')
#        line = f.readline()
#        while line:
#            print(line)
#            line = f.readline()
#        f.close()
      #  import_matrix_params['output_ws_name'] = params.get('workspace_name')
      #  import_matrix_params['output_obj_name'] = params.get('matrix_name')

#ref = self.fv.tsv_file_to_matrix(import_matrix_params)

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
