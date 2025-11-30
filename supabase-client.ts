import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://gabhllkyuzfptohcsjgr.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhYmhsbGt5dXpmcHRvaGNzamdyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIyNjE1MjQsImV4cCI6MjA3NzgzNzUyNH0.8dGc7LIg7oAJI4IxWv4cHNsOHA8p4zlkBG1MF9cTPzk'

export const supabase = createClient(supabaseUrl, supabaseKey)