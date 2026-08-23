import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://opcwwyzjvzykprbpyccb.supabase.co'
const supabaseKey = 'sb_publishable_yzM8m1BHN-i1KRf8bO5r9w_h-No9V8R'

export const supabase = createClient(supabaseUrl, supabaseKey)