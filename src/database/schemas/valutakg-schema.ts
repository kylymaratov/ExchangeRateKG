import { BankData } from '@/parser/format-data';
import { getDate } from '@/utils/get-date';
import { model, Schema } from 'mongoose';

const ValutaKgSchema = new Schema<{ parsedTime: Date; data: BankData[] }>({
  data: Array,
  parsedTime: Number,
});

export const ValutaKgModel = model('valutakg', ValutaKgSchema);
