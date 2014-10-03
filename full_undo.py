import sublime
import sublime_plugin

class FullUndo(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_timeout(self._full_undo, 100)

  def _full_undo(self):
    command = '[initital]'
    attempts = 0
    while command != '' and command != None:
      self.view.run_command('undo')
      command, _, _ = self.view.command_history(-1, True)
      attempts += 1
      if attempts > 1000: # preverse endless cycle; for sure
        raise Exception('Seems undo cycle is endless')

    self.view.run_command('undo')

class FullRedo(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_timeout(self._full_redo, 100)

  def _full_redo(self):
    command = '[initital]'
    attempts = 0
    while command != '' and command != None:
      self.view.run_command('redo')
      command, _, _ = self.view.command_history(1, True)
      attempts += 1
      if attempts > 1000: # preverse endless cycle; for sure
        raise Exception('Seems redo cycle is endless')

    self.view.run_command('redo')