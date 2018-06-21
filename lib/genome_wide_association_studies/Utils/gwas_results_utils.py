

import collections
import csv
import errno
import fileinput
import itertools
import json
import os
import re
import shutil
import subprocess
import time
import uuid
import zipfile

from KBaseReport.KBaseReportClient import KBaseReport
from DataFileUtil.DataFileUtilClient import DataFileUtil



def log(message, prefix_newline=False):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(('\n' if prefix_newline else '') + '{0:.2f}'.format(time.time()) + ': ' + str(message))


class gwas_results_utils:


    def _validate_params (Self, params):
            """
            Validate params
            """
            log ('Start validating params')

    def _mkdir_p(self, path):
        """
            _mkdir_p: make directory for given path
        """
        if not path:
            return
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def copyDirectory(self, src, dest):
            try:
                 shutil.copytree(src, dest)
                 # Directories are the same
            except shutil.Error as e:
                 print('Directory not copied. Error: %s' % e)
            # Any error saying that the directory doesn't exist
            except OSError as e:
                 print('Directory not copied. Error: %s' % e)


    def _run_command (self, command):
        """
          _run_command: run command and print result
        """
        log('Start executing command:\n{}'.format(command))
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output = pipe.communicate()[0]
        exit_code = pipe.returncode

        if exit_code == 0:
            log('Executed command:\n{}\n'.format(command) +
                          'Exit Code: {}\nOutput:\n{}'.format(exit_code, output))
        else:
            error_msg = 'Error running command:\n{}\n'.format(command)
            error_msg += 'Exit Code: {}\nOutput:\n{}'.format(exit_code, output)
            raise ValueError(error_msg)

    def _generate_html_report(self, template_directory, tsv_for_plot):
        log('start generating html report')
        html_report = list()

        output_directory = os.path.join(self.scratch, str(uuid.uuid4()))
        #self._mkdir_p(output_directory)
        
        self.copyDirectory(template_directory, output_directory)
        result_file_path = os.path.join(output_directory, 'index.html')


        shutil.copy2(tsv_for_plot,
                     os.path.join(output_directory, 'snpdata.tsv'))

        overview_content = 'This is overview'

        report_shock_id = self.dfu.file_to_shock({'file_path': output_directory,
                'pack': 'zip'})['shock_id']

        html_report.append({'shock_id': report_shock_id,
                'name': os.path.basename(result_file_path),
                'label': os.path.basename(result_file_path),
                'description': 'Manhattan plot'})
        return html_report

    def run_import_gwas_results(self, params):
        """
        Import GWAS results and display as manhattan plot
        """
        template_directory = "/kb/module/lib/genome_wide_association_studies/Utils/manhattan_plot_template"
        tsv_for_plot = "/kb/module/lib/genome_wide_association_studies/Utils/manhattan_plot_template/snpdata.tsv"
        output_html_files = self._generate_html_report (template_directory, tsv_for_plot)

        report_params = {
              'message': '',
              'workspace_name': params.get('workspace_name'),
              'file_links': [],
              'html_links': output_html_files,
              'direct_html_link_index': 0,
              'html_window_height': 333,
              'report_object_name': 'htmlreport_test_' + str(uuid.uuid4())}

        kbase_report_client = KBaseReport(self.callback_url)
        output = kbase_report_client.create_extended_report(report_params)

        report_output = {'report_name': output['name'], 'report_ref': output['ref']}

        return report_output

  

    def __init__(self, config):
        #self.ws_url = config["workspace-url"]
       # self.callback_url = config['SDK_CALLBACK_URL']
     #   self.token = config['KB_AUTH_TOKEN']
        #self.shock_url = config['shock-url']
        #self.gsu = GenomeSearchUtil(self.callback_url)
#        self.ws = Workspace(self.ws_url, token=self.token)
       # self.callbackURL = os.environ['SDK_CALLBACK_URL']
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.scratch = config['scratch']
        self.dfu = DataFileUtil(self.callback_url)






