'''
# Author: shawn.carrillo+sublime@gmail.com
# Source: https://github.com/scarrillo/GitUtils-Sublime
# Version 1.0
# Date: 2012.10.25
''' 
import sublime, sublime_plugin, os, subprocess, thread, time, tail, threading

class GitUtils(sublime_plugin.EventListener):
	def on_query_context(self, view, key, operator, operand, match_all):
		if key == "git_status":
			self.doGit(view)
			return True

		return None

	def doGit(self, view):
		projFolders = view.window().folders()
		for folder in projFolders:
			#view.window().run_command('exec', {"cmd": ["git", "--git-dir="+str(folder)+"/.git", "--work-tree="+str(folder), "status"]} )

			folderName = folder[folder.rfind('/')+1:]
			print "Git Status: "+folderName
			# Print git status
			log = os.popen("git --git-dir="+str(folder)+"/.git --work-tree="+str(folder)+ " status").readlines()
			# Print current branch
			#log = os.popen("git --git-dir="+str(folder)+"/.git --work-tree="+str(folder)+ " branch|grep \\*").readlines()
			if len(log) != 0:
				for line in log:
					print line