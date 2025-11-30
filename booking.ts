import { supabase } from './supabase-client'
import { PetService } from './types'

export async function insertAppointment(appointment: PetService) {
  const { data, error } = await supabase.from('PetServices').insert([appointment])
  if (error) throw new Error(error.message)
  return data
}