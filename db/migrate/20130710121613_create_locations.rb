class CreateLocations < ActiveRecord::Migration
  def change
    create_table :locations do |t|
      t.text :preferred_names
      t.text :aliases
      t.decimal :latitude, precision: 11, scale: 6
      t.decimal :longitude, precision: 11, scale: 6
      t.string :feature_class

      t.timestamps
    end
  end
end
